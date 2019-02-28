#!/usr/bin/env python
import sys

#get the size of the matrices from a size file:
info = open("matrix_size.txt").readlines()
for info_line in info:
    info_line = info_line.strip()
    matrix,i,j = info_line.split(",")
    if matrix == "A":
        #error prone type conversion
        try:
            A_i = int(i)
        except ValueError:
            continue
    else:
        try:
            B_j = int(j)
        except ValueError:
            continue

#actual mapping algorithm that needs A_i, B_i and text file as input
for line in sys.stdin:
    line = line.strip()
    matrix,i,j,v = line.split(",")

    if matrix == "A":
        for ind in range(1,B_j+1):
            key = i + "," + str(ind)
            print "%s\t%s\t%s"%(key,j,v)
            #we use tab to get rid of the problem of negative number
    else:
        for ind in range(1,A_i+1):
            key = str(ind) + "," + j
            print "%s\t%s\t%s"%(key,i,v)


###idea:
#1)add combiner, i.e. local aggregation
#2)implement normal matrix multiplication and test (i.e. triple for loop --> time O(n^3) , enormous memory consumption; as not distributed, no advantage of sparsity), 
# see http://www.joefkelley.com/853/ 
# also compare advantage of sparsity
#The first is based on the fact that if you store the matrixes as a tuples (i, j, x) meaning aij=x, 
#then the multiplication is equivalent to a relation algebra join followed by a group by and aggregation.
# 
# change log
# 1)   
