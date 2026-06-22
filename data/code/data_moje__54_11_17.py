import numpy as np

def create_hollow_square(size):
    if size <= 0:
        return np.array([])
    grid = np.zeros((size, size), dtype=np.uint8)
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
    result = create_hollow_square(sample_size)
    print(result)