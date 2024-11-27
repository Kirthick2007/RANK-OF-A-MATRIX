#Program to find the rank of a matrix.
#Developed by: Mohamed Riyaz Ahamed
#RegisterNumber: 24900085

import numpy as np
A = [[1,2,3],[3,6,9]]
sln = np.linalg.matrix_rank(A)
print(sln)
