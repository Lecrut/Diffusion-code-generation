def construct_repeating_grid(rows: int, cols: int) -> list:
    if rows <= 0 or cols <= 0:
        raise ValueError("Both rows and cols must be positive integers.")
    
    return [[(i * cols + j) % 5 for j in range(cols)] for i in range(rows)]

if __name__ == '__main__':
    sample_rows = 3
    sample_cols = 4
    grid = construct_repeating_grid(sample_rows, sample_cols)
    print(grid)