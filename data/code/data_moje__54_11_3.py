import numpy as np

def create_hollow_square(n):
    if n <= 0:
        raise ValueError("Size must be a positive integer")
    if n == 1:
        return np.array([[1]])
    grid = np.zeros((n, n), dtype=int)
    grid[0, :] = 1
    grid[-1, :] = 1
    grid[:, 0] = 1
    grid[:, -1] = 1
    return grid

if __name__ == '__main__':
    size = 5
    result = create_hollow_square(size)
    print(result)