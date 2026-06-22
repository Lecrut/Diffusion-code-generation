import numpy as np

def create_sequential_grid(size):
    if size <= 0:
        raise ValueError("Size must be greater than zero")
    return np.arange(size * size).reshape((size, size))

if __name__ == '__main__':
    grid = create_sequential_grid(4)
    print(grid)