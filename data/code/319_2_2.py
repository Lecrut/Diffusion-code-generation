def modify_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = i + j + 1
if __name__ == '__main__':
    sample_grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original Grid:")
    for row in sample_grid:
        print(row)
    modify_grid(sample_grid)
    print("\nModified Grid:")
    for row in sample_grid:
        print(row)