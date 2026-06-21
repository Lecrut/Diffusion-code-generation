def shortest_path_in_binary_matrix(grid):
    if not grid or not grid[0]:
        return -1
    
    rows = len(grid)
    cols = len(grid[0])
    
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1
    
    dp = [[-1 for _ in range(cols)] for _ in range(rows)]
    dp[0][0] = 0
    
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                continue
            
            if grid[i][j] == 1:
                dp[i][j] = -1
                continue
            
            min_prev = -1
            if i > 0 and dp[i - 1][j] != -1:
                min_prev = dp[i - 1][j]
            if j > 0 and dp[i][j - 1] != -1:
                prev_val = dp[i][j - 1]
                if min_prev == -1 or prev_val < min_prev:
                    min_prev = prev_val
            
            if min_prev != -1:
                dp[i][j] = min_prev + 1
            else:
                dp[i][j] = -1
    
    return dp[rows - 1][cols - 1]

if __name__ == '__main__':
    grid_sample = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    result = shortest_path_in_binary_matrix(grid_sample)
    print(result)
    
    grid_sample2 = [
        [0, 1, 0],
        [0, 0, 0]
    ]
    result2 = shortest_path_in_binary_matrix(grid_sample2)
    print(result2)
    
    grid_sample3 = [
        [1, 0],
        [0, 0]
    ]
    result3 = shortest_path_in_binary_matrix(grid_sample3)
    print(result3)