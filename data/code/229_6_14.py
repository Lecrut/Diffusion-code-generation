def generate_sum_grid(size):
    grid = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            grid[i][j] = i + j
    return grid

if __name__ == '__main__':
    sample_grid = generate_sum_grid(20)
    print(sample_grid)