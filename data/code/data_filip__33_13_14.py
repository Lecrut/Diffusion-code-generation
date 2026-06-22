def shortestPathBinaryMatrix(grid):
    if not grid or grid[0][0] != 0 or grid[-1][-1] != 0:
        return -1

    n = len(grid)
    if n == 1:
        return 1

    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                continue
            if i > 0 and dp[i - 1][j] != float('inf'):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
            if j > 0 and dp[i][j - 1] != float('inf'):
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
            if i > 0 and j > 0 and dp[i - 1][j - 1] != float('inf'):
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
            if i > 0 and j < n - 1 and dp[i - 1][j + 1] != float('inf'):
                dp[i][j] = min(dp[i][j], dp[i - 1][j + 1] + 1)
            if i < n - 1 and j > 0 and dp[i + 1][j - 1] != float('inf'):
                dp[i][j] = min(dp[i][j], dp[i + 1][j - 1] + 1)
            if i < n - 1 and dp[i + 1][j] != float('inf'):
                dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
            if i < n - 1 and j < n - 1 and dp[i + 1][j + 1] != float('inf'):
                dp[i][j] = min(dp[i][j], dp[i + 1][j + 1] + 1)

    return dp[n - 1][n - 1] if dp[n - 1][n - 1] != float('inf') else -1

if __name__ == '__main__':
    grid1 = [[0, 1], [1, 0]]
    grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    grid3 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(shortestPathBinaryMatrix(grid1))
    print(shortestPathBinaryMatrix(grid2))
    print(shortestPathBinaryMatrix(grid3))