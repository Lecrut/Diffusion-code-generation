import itertools

def construct_symbol_block(rows, cols, symbol):
    return '\n'.join(''.join(symbol for _ in range(cols)) for _ in range(rows))

if __name__ == '__main__':
    block = construct_symbol_block(3, 5, '*')
    print(block)