import numpy as np

def create_hollow_square(n):
    if n <= 0:
        return np.array([], dtype=int)
    if n == 1:
        return np.array([[1]], dtype=int)
    
    grid = np.zeros((n, n), dtype=int)
    grid[0, :] = 1
    grid[-1, :] = 1
    grid[:, 0] = 1
    grid[:, -1] = 1
    
    return grid

if __name__ == '__main__':
    sample_size = 5
    result = create_hollow_square(sample_size)
    print(result)