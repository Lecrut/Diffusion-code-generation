def fill_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            new_grid[i][j] = i + j
    return new_grid
if __name__ == '__main__':
    sample_grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result_grid = fill_grid(sample_grid)
    print(result_grid)