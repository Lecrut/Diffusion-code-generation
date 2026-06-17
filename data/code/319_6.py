def fill_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    indices = [[i + j for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = indices[i][j]
    return grid
if __name__ == '__main__':
    sample_grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result_grid = fill_grid(sample_grid)
    print(result_grid)