from typing import List

def construct_repeating_grid(rows: int, cols: int) -> List[List[int]]:
    return [[(i * cols + j) % 5 for j in range(cols)] for i in range(rows)]

if __name__ == '__main__':
    grid = construct_repeating_grid(4, 6)
    print(grid)