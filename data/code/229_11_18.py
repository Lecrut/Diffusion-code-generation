import numpy as np

def generate_square_grid(n):
    grid = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                grid[i, j] = 1
    return grid

if __name__ == '__main__':
    n_sample = 5
    result = generate_square_grid(n_sample)
    print(result)