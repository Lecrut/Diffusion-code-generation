def create_pattern(m, n):
    grid = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            grid[i][j] = (i + j) % 5
    return grid
if __name__ == '__main__':
    M = 4
    N = 5
    result = create_pattern(M, N)
    for row in result:
        print(row)