import numpy as np

def generate_square_grid(n):
    grid = np.zeros((n, n), dtype=int)
    for i in range(n):
        grid[i, ::2] = 1
        grid[i, 1::2] = 0
    return grid

if __name__ == '__main__':
    n_sample = 5
    result = generate_square_grid(n_sample)
    print(result)