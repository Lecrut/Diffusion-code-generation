def create_symbol_matrix(rows, cols, symbol):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("Rows must be a positive integer")
    if not isinstance(cols, int) or cols <= 0:
        raise ValueError("Columns must be a positive integer")
    if not isinstance(symbol, str) or len(symbol) != 1:
        raise ValueError("Symbol must be a single character")

    matrix = [[symbol for _ in range(cols)] for _ in range(rows)]
    return matrix

if __name__ == '__main__':
    rows_val = 5
    cols_val = 4
    symbol_val = '*'
    result = create_symbol_matrix(rows_val, cols_val, symbol_val)
    for row in result:
        print(''.join(row))