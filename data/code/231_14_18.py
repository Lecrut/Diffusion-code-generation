def construct_repeating_grid(rows: int, cols: int) -> list:
    pattern = [0, 1, 2, 3, 4]
    grid = [[pattern[(i * cols + j) % len(pattern)] for j in range(cols)] for i in range(rows)]
    return grid

if __name__ == '__main__':
    rows = 5
    cols = 6
    grid = construct_repeating_grid(rows, cols)
    for row in grid:
        print(row)