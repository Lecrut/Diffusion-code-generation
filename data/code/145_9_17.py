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
            if matrix[r][c] and not visited[r][c]:
                dfs(r, c)
                break

    return any(any(row) for row in visited)

if __name__ == '__main__':
    sample_matrix = [
        [True, False, True],
        [False, True, False],
        [True, False, True]
    ]
    print(is_reachable(sample_matrix))