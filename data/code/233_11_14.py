def generate_symbol_matrix(rows, cols, symbol):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("Rows must be a positive integer.")
    if not isinstance(cols, int) or cols <= 0:
        raise ValueError("Columns must be a positive integer.")
    if not isinstance(symbol, str) or len(symbol) != 1:
        raise ValueError("Symbol must be a single character string.")

    matrix = []
    for _ in range(rows):
        row = [symbol] * cols
        matrix.append(row)
    
    return '\n'.join(' '.join(row) for row in matrix)

if __name__ == '__main__':
    try:
        result = generate_symbol_matrix(5, 10, '*')
        print(result)
    except ValueError as e:
        print(e)