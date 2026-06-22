def validate_inputs(rows, cols, symbol):
    if not (isinstance(rows, int) and rows > 0):
        raise ValueError("Rows must be a positive integer")
    if not (isinstance(cols, int) and cols > 0):
        raise ValueError("Columns must be a positive integer")
    if not isinstance(symbol, str) or len(symbol) != 1:
        raise ValueError("Symbol must be a single character string")

def build_row(col_count, symbol):
    return symbol * col_count

def rectangle_generator(rows, cols, symbol):
    validate_inputs(rows, cols, symbol)
    for _ in range(rows):
        yield build_row(cols, symbol)

if __name__ == '__main__':
    R = 5
    C = 10
    S = '*'
    generator = rectangle_generator(R, C, S)
    result_list = list(generator)
    print(result_list)