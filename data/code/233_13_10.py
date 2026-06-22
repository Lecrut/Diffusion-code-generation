import itertools

def construct_symbol_block(rows, cols, symbol):
    return '\n'.join(symbol * cols for _ in range(rows))

if __name__ == '__main__':
    sample_block = construct_symbol_block(3, 4, '*')
    print(sample_block)