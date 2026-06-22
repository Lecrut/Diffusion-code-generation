import numpy as np

def create_hollow_square(n):
    if n <= 0:
        raise ValueError("Size must be a positive integer")
    grid = np.ones((n, n), dtype=int)
    if n > 2:
        grid[1:-1, 1:-1] = 0
    return grid

if __name__ == '__main__':
    sample_size = 5
    result = create_hollow_square(sample_size)
    print(result)