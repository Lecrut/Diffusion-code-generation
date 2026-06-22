from typing import List

def construct_repeating_grid(rows: int, cols: int) -> List[List[int]]:
    pattern = [0, 1, 2, 3, 4]
    return [[pattern[(i * cols + j) % len(pattern)] for j in range(cols)] for i in range(rows)]

if __name__ == '__main__':
    result = construct_repeating_grid(3, 5)
    print(result)