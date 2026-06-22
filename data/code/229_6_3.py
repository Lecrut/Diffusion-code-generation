def create_sum_grid(size):
    grid = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            grid[i][j] = i + j
    return grid

if __name__ == '__main__':
    N = 15
    sum_grid = create_sum_grid(N)
    for row in sum_grid:
        print(row)