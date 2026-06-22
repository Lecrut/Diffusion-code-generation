import itertools

def create_symbol_block(rows, cols, symbol):
    return '\n'.join(''.join(symbol for _ in range(cols)) for _ in range(rows))

if __name__ == '__main__':
    block = create_symbol_block(3, 4, '*')
    print(block)