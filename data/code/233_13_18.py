import itertools

def construct_symbol_block(rows, cols, symbol):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("Rows must be a positive integer.")
    if not isinstance(cols, int) or cols <= 0:
        raise ValueError("Cols must be a positive integer.")
    
    block = list(itertools.product(range(rows), range(cols)))
    return '\n'.join(symbol * len(row) for row in block)

if __name__ == '__main__':
    try:
        sample_block = construct_symbol_block(3, 4, '*')
        print(sample_block)
    except ValueError as e:
        print(e)