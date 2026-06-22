from typing import List

def construct_repeating_grid(rows: int, cols: int) -> List[List[int]]:
    pattern = [i % 5 for i in range(20)]
    grid = [[pattern[(i * cols + j) % len(pattern)] for j in range(cols)] for i in range(rows)]
    return grid

if __name__ == '__main__':
    rows, cols = 4, 5
    if not isinstance(rows, int) or not isinstance(cols, int):
        raise ValueError("Both rows and cols must be integers.")
    if rows < 1 or cols < 1:
        raise ValueError("Rows and cols must be positive integers.")

    grid = construct_repeating_grid(rows, cols)
    for row in grid:
        print(row)