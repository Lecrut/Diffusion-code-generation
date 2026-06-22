import itertools

def construct_symbol_block(rows, cols, symbol):
    return '\n'.join(symbol * cols for _ in range(rows))

if __name__ == '__main__':
    rows = 6
    cols = 7
    symbol = '#'
    
    block = construct_symbol_block(rows, cols, symbol)
    print(block)