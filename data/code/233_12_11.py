import numpy as np

class Rectangle:
    def __init__(self, width, height, symbol):
        self.width = width
        self.height = height
        self.symbol = symbol
        self.grid = np.full((height, width), self.symbol)

    def draw(self):
        print("\n".join("".join(row) for row in self.grid))

if __name__ == '__main__':
    rect1 = Rectangle(5, 3, '*')
    rect1.draw()
    print("-" * 10)
    rect2 = Rectangle(8, 2, '#')
    rect2.draw()
    print("-" * 10)
    rect3 = Rectangle(4, 4, '@')
    rect3.draw()