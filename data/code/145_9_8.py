def is_reachable(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] == False or visited[row][col]:
            return
        visited[row][col] = True
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)
    
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] and not visited[row][col]:
                dfs(row, col)
                return True
    return False

if __name__ == '__main__':
    sample_matrix = [
        [True, False, True],
        [False, True, False],
        [True, False, True]
    ]
    print(is_reachable(sample_matrix))