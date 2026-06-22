import numpy as np
GRID_SIZE = 5

def generate_square_grid(n):
    return np.fromfunction(lambda i, j: (i + j) % 2, (n, n))
if __name__ == '__main__':
    result = generate_square_grid(GRID_SIZE)
    print(result)