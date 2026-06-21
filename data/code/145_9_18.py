ROWS = 3
COLS = 3

def is_reachable(matrix):
    visited = [[False] * COLS for _ in range(ROWS)]

    def dfs(row, col):
        if row < 0 or row >= ROWS or col < 0 or (col >= COLS) or (matrix[row][col] == False) or visited[row][col]:
            return
        visited[row][col] = True
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)
    for i in range(ROWS):
        for j in range(COLS):
            if matrix[i][j] == True and (not visited[i][j]):
                dfs(i, j)
    for row in range(ROWS):
        for col in range(COLS):
            if matrix[row][col] == True and (not visited[row][col]):
                return False
    return True
if __name__ == '__main__':
    sample_matrix = [[True, False, True], [False, True, False], [True, False, True]]
    print(is_reachable(sample_matrix))