import numpy as np

class ASCIIRectangle:
    def __init__(self, width, height, symbol):
        self.width = width
        self.height = height
        self.symbol = symbol

    def create_rectangle(self):
        return np.full((self.height, self.width), self.symbol, dtype=str)

    def print_rectangle(self):
        rectangle = self.create_rectangle()
        for line in rectangle:
            print("".join(line))

if __name__ == '__main__':
    rect1 = ASCIIRectangle(5, 3, '*')
    rect1.print_rectangle()
    print("-" * 10)
    rect2 = ASCIIRectangle(8, 2, '#')
    rect2.print_rectangle()
    print("-" * 10)
    rect3 = ASCIIRectangle(4, 4, '@')
    rect3.print_rectangle()