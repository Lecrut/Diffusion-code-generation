import numpy as np

def create_square_grid(size):
    return np.arange(size * size).reshape(size, size)

if __name__ == '__main__':
    grid = create_square_grid(4)
    print(grid)