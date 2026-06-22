def create_wrapping_grid(rows, cols):
    total_cells = rows * cols
    grid = [[0] * cols for _ in range(rows)]
    num = 1

    for i in range(total_cells):
        row = i // cols
        col = i % cols
        grid[row][col] = num
        num += 1

    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(f'{cell:2d}' for cell in row))

if __name__ == '__main__':
    sample_rows, sample_cols = 4, 5
    wrapping_grid = create_wrapping_grid(sample_rows, sample_cols)
    print_grid(wrapping_grid)