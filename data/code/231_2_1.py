import numpy as np
def generate_diagonal_pattern(limit):
    n = int(np.sqrt(limit))
    if n * n < limit:
        n += 1
    grid = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if i == j:
                grid[i, j] = (i * n) + j + 1
            else:
                pass
    return grid
if __name__ == '__main__':
    sample_limit = 25
    pattern = generate_diagonal_pattern(sample_limit)
    print(pattern)