def generate_grid(rows, cols):
    N = rows * cols
    grid = [[0] * cols for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = num
            num += 1
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(str(cell).ljust(3) for cell in row))

if __name__ == '__main__':
    sample_rows = 4
    sample_cols = 5
    grid = generate_grid(sample_rows, sample_cols)
    print_grid(grid)