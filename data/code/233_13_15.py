import itertools

class SymbolBlock:
    def __init__(self, rows, cols, symbol):
        self.rows = rows
        self.cols = cols
        self.symbol = symbol

    def construct_block(self):
        block = list(itertools.product(range(self.rows), range(self.cols)))
        return '\n'.join(self.symbol * len(row) for row in block)

if __name__ == '__main__':
    sample_block = SymbolBlock(3, 4, '*')
    print(sample_block.construct_block())