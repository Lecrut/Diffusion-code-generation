import numpy as np
def fill_grid_pattern(rows, cols, pattern):
    grid = np.zeros((rows, cols), dtype=int)
    for r in range(rows):
        for c in range(cols):
            grid[r, c] = pattern[r % len(pattern)]
    return grid
if __name__ == '__main__':
    ROWS = 10
    COLS = 12
    PATTERN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result_grid = fill_grid_pattern(ROWS, COLS, PATTERN)
    print("Resulting Grid:")
    print(result_grid)