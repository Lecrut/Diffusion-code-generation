def is_reachable(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] == False or visited[r][c]:
            return
        visited[r][c] = True
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == True and not visited[r][c]:
                dfs(r, c)

    return any(visited[r][0] or visited[r][-1] for r in range(rows)) or any(visited[0][c] or visited[-1][c] for c in range(cols))

if __name__ == '__main__':
    sample_matrix = [
        [True, False, True],
        [False, True, False],
        [True, False, True]
    ]
    print(is_reachable(sample_matrix))