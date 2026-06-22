import numpy as np

def construct_hollow_square_grid(size):
    grid = np.zeros((size, size), dtype=int)
    if size > 1:
        grid[0, :] = 1
        grid[-1, :] = 1
        grid[:, 0] = 1
        grid[:, -1] = 1
    return grid

if __name__ == '__main__':
    result = construct_hollow_square_grid(5)
    print(result)