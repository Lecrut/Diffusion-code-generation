class RectangleGenerator:
    def __init__(self, rows, cols, symbol):
        self.rows = rows
        self.cols = cols
        self.symbol = symbol

    def generate(self):
        return '\n'.join([self.symbol * self.cols for _ in range(self.rows)])

if __name__ == '__main__':
    R = 5
    C = 10
    S = '*'
    rect_gen = RectangleGenerator(R, C, S)
    print(rect_gen.generate())