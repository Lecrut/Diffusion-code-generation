import numpy as np

def construct_hollow_square(size: int) -> np.ndarray:
    if size <= 0:
        return np.array([])
    grid = np.zeros((size, size), dtype=int)
    grid[0, :] = 1
    grid[-1, :] = 1
    grid[:, 0] = 1
    grid[:, -1] = 1
    return grid

if __name__ == '__main__':
    result = construct_hollow_square(5)
    print(result)