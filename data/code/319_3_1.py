def create_grid(n):
    grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            grid[i][j] = i * j
    return grid
if __name__ == '__main__':
    N = 5
    result_grid = create_grid(N)
    for row in result_grid:
        print(row)