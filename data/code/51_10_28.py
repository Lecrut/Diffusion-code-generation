class Rectangle:
    DEFAULT_WIDTH = 5.0
    DEFAULT_HEIGHT = 3.0

    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        self.width = width
        self.height = height

    @staticmethod
    def calculate_perimeter(width, height):
        return 2 * (width + height)

    def perimeter(self):
        return Rectangle.calculate_perimeter(self.width, self.height)

if __name__ == '__main__':
    rect1 = Rectangle(7.5, 2.0)
    print(rect1.perimeter())

    rect2 = Rectangle()
    print(rect2.perimeter())