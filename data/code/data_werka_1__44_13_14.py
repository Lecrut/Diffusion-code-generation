class Rectangle:
    DEFAULT_LENGTH = 10
    DEFAULT_WIDTH = 5

    @staticmethod
    def calculate_perimeter(length=DEFAULT_LENGTH, width=DEFAULT_WIDTH):
        return 2 * (length + width)

if __name__ == '__main__':
    perimeter = Rectangle.calculate_perimeter()
    print(perimeter)