class Rectangle:
    DEFAULT_WIDTH = 5
    DEFAULT_HEIGHT = 10

    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        self.width = width
        self.height = height

    @staticmethod
    def calculate_perimeter(width, height):
        return 2 * (width + height)

if __name__ == '__main__':
    rect1 = Rectangle()
    perimeter1 = Rectangle.calculate_perimeter(rect1.width, rect1.height)
    print(perimeter1)

    rect2 = Rectangle(8, 6)
    perimeter2 = Rectangle.calculate_perimeter(rect2.width, rect2.height)
    print(perimeter2)