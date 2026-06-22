class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)
if __name__ == '__main__':
    rect1 = Rectangle(5, 3)
    print(rect1.perimeter())
    rect2 = Rectangle(7, 4)
    print(rect2.perimeter())