from typing import List

def construct_repeating_grid(rows: int, cols: int) -> List[List[int]]:
    if not isinstance(rows, int) or not isinstance(cols, int):
        raise ValueError("Both rows and cols must be integers.")
    if rows < 1 or cols < 1:
        raise ValueError("Both rows and cols must be positive integers.")

    return [[(i * cols + j) % 5 for j in range(cols)] for i in range(rows)]

if __name__ == '__main__':
    grid = construct_repeating_grid(3, 4)
    print(grid)