def fill_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = i + j
if __name__ == '__main__':
    sample_grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original Grid:")
    for row in sample_grid:
        print(row)
    fill_grid(sample_grid)
    print("\nFilled Grid (grid[i][j] = i + j):")
    for row in sample_grid:
        print(row)