import numpy as np

def create_sequential_grid(size):
    return np.arange(size**2).reshape(size, size)

if __name__ == '__main__':
    grid = create_sequential_grid(4)
    print(grid)