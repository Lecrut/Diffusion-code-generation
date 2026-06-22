import numpy as np

SYMBOL = '@'
WIDTH = 5
HEIGHT = 3

def fill_rectangle(symbol=SYMBOL, width=WIDTH, height=HEIGHT):
    return np.full((height, width), symbol, dtype=str)

if __name__ == '__main__':
    filled_rect = fill_rectangle()
    print('\n'.join([''.join(row) for row in filled_rect]))