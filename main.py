import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2],
             [3, 4]])

B = np.array([[5, 6],
             [7, 8]])

# print matrix information
print(f'Shape of A (rows, columns):  {A.shape}')
print(f'Dimensions of A:  {A.ndim}')
print(f'Size of A:  {A.size} elements')
print(f'Type in A:  {A.dtype}')
print(f'Item size in A:  {A.itemsize} bytes')

# Matrix Operations (elementwise)
# 1. compute addition
add = A + B
print(f'\nAddition: {add}')

# 2. compute difference
diff = A - B
print(f'Difference: {diff}')

# 3. compute matrix multiplication
multiply = A @ B
print(f'Multiplication: {multiply}')

# 4. compute matrix multiplication (elementwise)
multiply_elements = A * B
print(f'Multiplication (elementwise): {multiply_elements}')

# 5. compute dot product (scalar quantity, magnitude)
# Note: how much two vectors point in the same direction
# Important: if zero, two vectors are perpendicular
dot = A.dot(B)
print(f'Dot Product: {dot}')

# 6. cross product (vector quantity, magnitude and direction)
# Note: how much two vectors point in different directions
# Note: right hand rule determines sign (positive or negative)
# Note: cross product done on each row of matrices
# Important: if zero, two vectors are parallel
cross = np.cross(A, B)
print(f'Cross Product: {cross}')

# plot matrix
