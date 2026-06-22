class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    rect = Rectangle(5, 3)
    print(Rectangle.perimeter(rect.length, rect.width))