import numpy as np

def create_hollow_square_grid(size):
    grid = np.zeros((size, size), dtype=int)
    if size <= 0:
        return grid
    grid[0, :] = 1
    grid[-1, :] = 1
    if size > 1:
        grid[1:-1, 0] = 1
        grid[1:-1, -1] = 1
    return grid

if __name__ == '__main__':
    size = 5
    result = create_hollow_square_grid(size)
    print(result)