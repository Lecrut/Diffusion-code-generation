import numpy as np
def fill_matrix_pattern(rows, cols, pattern):
    matrix = np.zeros((rows, cols), dtype=int)
    for r in range(rows):
        for c in range(cols):
            index = r * cols + c
            matrix[r, c] = pattern[index % len(pattern)]
    return matrix
if __name__ == '__main__':
    ROWS = 5
    COLS = 6
    PATTERN_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result_matrix = fill_matrix_pattern(ROWS, COLS, PATTERN_VALUES)
    print(result_matrix)