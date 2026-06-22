import itertools
SYMBOL = '*'
WIDTH = 10
HEIGHT = 5

def draw_rectangle(width, height, symbol):
    block = list(itertools.product(range(height), range(width)))
    return '\n'.join((symbol * len(row) if y == 0 or y == height - 1 else symbol + ' ' * (width - 2) + symbol for y, row in block))
if __name__ == '__main__':
    sample_block = draw_rectangle(WIDTH, HEIGHT, SYMBOL)
    print(sample_block)