def generate_grid():
    grid = [[0] * 20 for _ in range(20)]
    for i in range(20):
        for j in range(20):
            grid[i][j] = i + j
    return grid

if __name__ == '__main__':
    sample_grid = generate_grid()
    print(sample_grid)