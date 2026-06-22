import numpy as np

def create_hollow_square(size):
    if size <= 0:
        return np.empty((0, 0), dtype=int)
    grid = np.zeros((size, size), dtype=int)
    if size == 1:
        grid[0, 0] = 1
    else:
        grid[0, :] = 1
        grid[-1, :] = 1
        grid[:, 0] = 1
        grid[:, -1] = 1
    return grid

if __name__ == '__main__':
    size = 5
    result = create_hollow_square(size)
    print(result)