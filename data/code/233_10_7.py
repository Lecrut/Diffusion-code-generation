class GridFiller:
    def __init__(self, width, height, symbol):
        self.width = width
        self.height = height
        self.symbol = symbol

    def fill(self):
        return '\n'.join([''.join([self.symbol for _ in range(self.width)]) for _ in range(self.height)])

if __name__ == '__main__':
    filler = GridFiller(10, 5, '*')
    print(filler.fill())