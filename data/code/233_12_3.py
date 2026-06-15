class Rectangle:
    def __init__(self, width, height, symbol):
        self.width = width
        self.height = height
        self.symbol = symbol
    def draw(self):
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                if x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1:
                    line += self.symbol
                else:
                    line += " "
            print(line)
if __name__ == '__main__':
    rect1 = Rectangle(5, 5, "#")
    print("Rectangle 1:")
    rect1.draw()
    print("\n" + "="*10 + "\n")
    rect2 = Rectangle(8, 4, "@")
    print("Rectangle 2:")
    rect2.draw()