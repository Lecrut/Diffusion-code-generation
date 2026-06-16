def create_pattern(M, N):
    grid = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            grid[i][j] = (i + j) % 5
    return grid
if __name__ == '__main__':
    M_sample = 4
    N_sample = 5
    result = create_pattern(M_sample, N_sample)
    for row in result:
        print(row)