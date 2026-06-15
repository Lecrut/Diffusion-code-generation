class Rectangle:
    def __init__(self, width, height, symbol):
        self.width = width
        self.height = height
        self.symbol = symbol
    def draw(self):
        for _ in range(self.height):
            print(self.symbol * self.width)
if __name__ == '__main__':
    rect1 = Rectangle(5, 3, '*')
    rect1.draw()
    print("-" * 10)
    rect2 = Rectangle(8, 2, '#')
    rect2.draw()
    print("-" * 10)
    rect3 = Rectangle(4, 4, '@')
    rect3.draw()