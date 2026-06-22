def shortest_path(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return -1
    
    rows = len(grid)
    cols = len(grid[0])
    
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1
    
    dp = [[-1] * cols for _ in range(rows)]
    dp[0][0] = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dp[r][c] = -1
                continue
            if r == 0 and c == 0:
                continue
            
            min_prev = -1
            
            if r > 0 and dp[r - 1][c] != -1:
                min_prev = dp[r - 1][c]
            if c > 0 and dp[r][c - 1] != -1:
                if min_prev == -1 or dp[r][c - 1] < min_prev:
                    min_prev = dp[r][c - 1]
            
            if min_prev != -1:
                dp[r][c] = min_prev + 1
            else:
                dp[r][c] = -1
                
    return dp[rows - 1][cols - 1]

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    result = shortest_path(sample_grid)
    print(result)