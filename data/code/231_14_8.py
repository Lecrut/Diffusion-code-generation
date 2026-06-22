from typing import List

def construct_repeating_grid(rows: int, cols: int) -> List[List[int]]:
    if not isinstance(rows, int) or not isinstance(cols, int):
        raise ValueError("Both rows and cols must be integers.")
    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and cols must be positive integers.")

    pattern = [i % 5 for i in range(20)]
    grid = [[pattern[(i * cols + j) % len(pattern)] for j in range(cols)] for i in range(rows)]
    return grid

if __name__ == '__main__':
    rows = 3
    cols = 4
    result = construct_repeating_grid(rows, cols)
    print(result)