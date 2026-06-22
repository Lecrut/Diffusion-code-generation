class Rectangle:
    DEFAULT_WIDTH = 5
    DEFAULT_HEIGHT = 3

    @staticmethod
    def calculate_perimeter(width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        return 2 * (width + height)

if __name__ == '__main__':
    perimeter = Rectangle.calculate_perimeter()
    print(perimeter)