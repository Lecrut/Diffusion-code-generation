def shortest_path_grid(grid):
    m = len(grid)
    n = len(grid[0])
    
    if grid[0][0] == 1 or grid[m-1][n-1] == 1:
        return -1
    
    dp = [[-1] * n for _ in range(m)]
    dp[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = -1
                continue
            
            if i > 0 and dp[i-1][j] != -1:
                if dp[i][j] == -1 or dp[i-1][j] < dp[i][j]:
                    dp[i][j] = dp[i-1][j] + 1
            
            if j > 0 and dp[i][j-1] != -1:
                if dp[i][j] == -1 or dp[i][j-1] < dp[i][j]:
                    dp[i][j] = dp[i][j-1] + 1
    
    return dp[m-1][n-1] if dp[m-1][n-1] != -1 else -1

if __name__ == '__main__':
    grid1 = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    print(shortest_path_grid(grid1))

    grid2 = [
        [0, 1],
        [0, 0]
    ]
    print(shortest_path_grid(grid2))

    grid3 = [
        [0, 0],
        [0, 0]
    ]
    print(shortest_path_grid(grid3))