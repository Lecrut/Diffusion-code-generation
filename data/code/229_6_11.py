def generate_sum_grid(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError('Size must be a positive integer')
    grid = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            grid[i][j] = i + j
    return grid
if __name__ == '__main__':
    try:
        sample_grid = generate_sum_grid(20)
        for row in sample_grid[:5]:
            print(row)
    except ValueError as e:
        print(e)