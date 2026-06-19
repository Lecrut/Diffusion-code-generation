class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect1 = Rectangle(8, 4)
    print(rect1.perimeter())

    rect2 = Rectangle(12, 6)
    print(rect2.perimeter())