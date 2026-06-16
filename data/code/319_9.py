def fill_grid_dfs(R, C):
    grid = [[0] * C for _ in range(R)]
    count = 1
    def dfs(r, c):
        nonlocal count
        if r >= R:
            return
        if r < 0 or c >= C:
            return
        grid[r][c] = count
        count += 1
        dfs(r + 1, c)
        dfs(r, c + 1)
    dfs(0, 0)
    return grid
if __name__ == '__main__':
    R_sample = 3
    C_sample = 4
    result_grid = fill_grid_dfs(R_sample, C_sample)
    for row in result_grid:
        print(row)