import numpy as np

def create_hollow_square(size):
    if size < 1:
        return np.array([])
    grid = np.zeros((size, size), dtype=int)
    if size == 1:
        grid[0, 0] = 1
        return grid
    grid[0, :] = 1
    grid[-1, :] = 1
    grid[:, 0] = 1
    grid[:, -1] = 1
    return grid

if __name__ == '__main__':
    sample_size = 5
    result_grid = create_hollow_square(sample_size)
    print(result_grid)