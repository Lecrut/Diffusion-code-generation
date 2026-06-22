import numpy as np

def create_square_grid(size):
    return np.fromfunction(lambda i, j: (i + j) % 2, (size, size))

if __name__ == '__main__':
    grid = create_square_grid(5)
    print(grid)