class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def perimeter(rectangle):
        return 2 * (rectangle.length + rectangle.width)

if __name__ == '__main__':
    rect = Rectangle(5, 3)
    print(Rectangle.perimeter(rect))