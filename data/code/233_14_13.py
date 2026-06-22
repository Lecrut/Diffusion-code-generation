class SymbolRectangle:
    def __init__(self, rows, cols, symbol):
        self.rows = rows
        self.cols = cols
        self.symbol = symbol

    def generate_row(self):
        return self.symbol * self.cols

    def generate_rectangle(self):
        return '\n'.join([self.generate_row() for _ in range(self.rows)])

if __name__ == '__main__':
    R = 5
    C = 10
    S = '*'
    rect = SymbolRectangle(R, C, S)
    print(rect.generate_rectangle())