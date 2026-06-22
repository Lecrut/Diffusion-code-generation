class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def perimeter(width, height):
        return 2 * (width + height)

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(Rectangle.perimeter(rect.width, rect.height))