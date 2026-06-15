import numpy as np
def generate_diagonal_pattern(limit):
    n = limit * limit
    pattern = np.arange(1, limit + 1)
    indices = np.arange(limit)
    rows = np.zeros((limit, limit), dtype=int)
    for i in range(limit):
        row_start = i
        row_end = limit - 1 - i
        if row_start <= row_end:
            for j in range(row_start, row_end + 1):
                rows[i, j] = limit - (j - row_start)
    return rows
if __name__ == '__main__':
    limit_val = 5
    result = generate_diagonal_pattern(limit_val)
    print(result)