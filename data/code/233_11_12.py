def create_matrix(rows, cols, symbol):
    if not all(isinstance(x, int) and x > 0 for x in [rows, cols]):
        raise ValueError("Rows and columns must be positive integers")
    if not isinstance(symbol, str) or len(symbol) != 1:
        raise ValueError("Symbol must be a single character")

    matrix = [[symbol] * cols for _ in range(rows)]
    return matrix

if __name__ == '__main__':
    rows_val = 4
    cols_val = 5
    symbol_val = '#'
    result = create_matrix(rows_val, cols_val, symbol_val)
    print(result)