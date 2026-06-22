class RectangleFiller:
    def __init__(self, width, height, symbol):
        self.width = width
        self.height = height
        self.symbol = symbol

    def fill(self):
        return [([self.symbol] * self.width) for _ in range(self.height)]

if __name__ == '__main__':
    filler = RectangleFiller(10, 5, '*')
    grid = filler.fill()
    print(grid)