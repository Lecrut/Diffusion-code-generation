import itertools

def construct_symbol_block(rows, cols, symbol):
    block = list(itertools.product(range(rows), range(cols)))
    return '\n'.join(symbol * len(row) for row in block)

if __name__ == '__main__':
    sample_block = construct_symbol_block(3, 4, '*')
    print(sample_block)