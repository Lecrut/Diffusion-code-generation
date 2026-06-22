def create_symbol_grid(rows, cols, symbol):
    grid = []
    for i in range(rows):
        row = [symbol] * cols
        grid.append(row)
    return grid

if __name__ == '__main__':
    matrix_rows = 6
    matrix_cols = 8
    symbol_char = '@'
    result_grid = create_symbol_grid(matrix_rows, matrix_cols, symbol_char)
    for row in result_grid:
        print(''.join(row))