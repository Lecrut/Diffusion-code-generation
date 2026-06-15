import numpy as np
def generate_diagonal_pattern(n):
    if n <= 0:
        return np.array([])
    size = int(np.ceil(np.sqrt(n)))
    grid = np.zeros((size, size), dtype=np.int32)
    for i in range(size):
        for j in range(size):
            if i * size + j < n:
                grid[i, j] = i * size + j + 1
            else:
                break
    return grid
if __name__ == '__main__':
    limit = 25
    pattern = generate_diagonal_pattern(limit)
    print(pattern)