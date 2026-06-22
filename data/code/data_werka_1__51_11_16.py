class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect1 = Rectangle(3, 4)
    print(f"Perimeter of rect1: {rect1.perimeter()}")
    rect2 = Rectangle(10.5, 2.5)
    print(f"Perimeter of rect2: {rect2.perimeter()}")