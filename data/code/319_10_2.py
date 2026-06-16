import numpy as np
def fill_matrix_pattern(rows, cols, pattern):
    matrix = np.zeros((rows, cols), dtype=int)
    for r in range(rows):
        for c in range(cols):
            matrix[r, c] = pattern[r % len(pattern)]
    return matrix
if __name__ == '__main__':
    ROWS = 5
    COLS = 8
    PATTERN = [1, 2, 3, 4, 5]
    result_matrix = fill_matrix_pattern(ROWS, COLS, PATTERN)
    print("Result Matrix:")
    print(result_matrix)