def create_rectangle(rows, cols, symbol):
    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be positive integers.")
    if not isinstance(symbol, str) or len(symbol) != 1:
        raise ValueError("Symbol must be a single character string.")

    row = symbol * cols
    rectangle = [row] * rows
    return rectangle

if __name__ == '__main__':
    R = 5
    C = 10
    S = '*'
    result = create_rectangle(R, C, S)
    for row in result:
        print(row)