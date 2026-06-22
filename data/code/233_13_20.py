import itertools

def validate_dimensions(width, height):
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer.")
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer.")

def construct_symbol_block(rows, cols, symbol):
    validate_dimensions(cols, rows)
    block = itertools.product(range(rows), range(cols))
    return '\n'.join(symbol * len(row) for row in block)

if __name__ == '__main__':
    width = 10
    height = 5
    symbol = "*"
    try:
        sample_block = construct_symbol_block(width, height, symbol)
        print(sample_block)
    except ValueError as e:
        print(e)