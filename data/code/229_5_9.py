import numpy as np

def create_sequential_grid(size):
    return np.arange(size * size).reshape(size, size)

if __name__ == '__main__':
    sample_size = 4
    grid = create_sequential_grid(sample_size)
    print(grid)