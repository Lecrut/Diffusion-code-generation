from typing import List

def construct_repeating_grid(rows: int, cols: int) -> List[List[int]]:
    if not (isinstance(rows, int) and isinstance(cols, int)):
        raise ValueError("Both rows and cols must be integers.")
    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and cols must be greater than zero.")
    
    return [[(i * cols + j) % 5 for j in range(cols)] for i in range(rows)]

if __name__ == '__main__':
    grid = construct_repeating_grid(3, 4)
    print(grid)