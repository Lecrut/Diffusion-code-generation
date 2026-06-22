class Rectangle:
    def __init__(self, width, height, symbol):
        self.width = width
        self.height = height
        self.symbol = symbol

    def generate_grid(self):
        return [self.symbol * self.width for _ in range(self.height)]

if __name__ == '__main__':
    rect = Rectangle(5, 3, '*')
    grid = rect.generate_grid()
    for row in grid:
        print(row)