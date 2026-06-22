import itertools

def validate_rectangle_params(width, height):
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer.")
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer.")

def construct_symbol_block(rows, cols, symbol):
    validate_rectangle_params(rows, cols)
    block = list(itertools.product(range(rows), range(cols)))
    return '\n'.join(symbol for _ in range(len(block)))

if __name__ == '__main__':
    width = 10
    height = 5
    symbol = "*"
    try:
        block = construct_symbol_block(width, height, symbol)
        print(block)
    except ValueError as e:
        print(e)