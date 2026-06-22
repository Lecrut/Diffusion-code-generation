import numpy as np

def create_hollow_square_grid(size):
    if size <= 0:
        return np.array([])
    if size == 1:
        return np.array([[1]])
    
    grid = np.zeros((size, size), dtype=int)
    grid[0, :] = 1
    grid[-1, :] = 1
    grid[:, 0] = 1
    grid[:, -1] = 1
    return grid

if __name__ == '__main__':
    sample_size = 5
    result = create_hollow_square_grid(sample_size)
    print(result)