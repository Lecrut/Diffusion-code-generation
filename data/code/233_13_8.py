import itertools

SYMBOL = '*'
WIDTH = 10
HEIGHT = 5

def construct_symbol_block(width=WIDTH, height=HEIGHT, symbol=SYMBOL):
    return '\n'.join(''.join(symbol for _ in range(width)) for _ in range(height))

if __name__ == '__main__':
    block = construct_symbol_block()
    print(block)