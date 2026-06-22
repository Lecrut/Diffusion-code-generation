import itertools

class SymbolBlock:
    def __init__(self, rows, cols, symbol):
        self.rows = rows
        self.cols = cols
        self.symbol = symbol
        self.block = list(itertools.product(range(rows), range(cols)))

    def generate_block(self):
        return '\n'.join(self.symbol * len(row) for row in self.block)

if __name__ == '__main__':
    block = SymbolBlock(3, 4, '*')
    print(block.generate_block())