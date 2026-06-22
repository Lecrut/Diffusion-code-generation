import numpy as np

def create_sequential_grid(size):
    return np.arange(size * size).reshape((size, size))

if __name__ == '__main__':
    grid_size = 4
    sequential_grid = create_sequential_grid(grid_size)
    print(sequential_grid)