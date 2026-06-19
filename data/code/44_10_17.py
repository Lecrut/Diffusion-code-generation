class Rectangle:
    DEFAULT_LENGTH = 12
    DEFAULT_WIDTH = 6

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    length = Rectangle.DEFAULT_LENGTH
    width = Rectangle.DEFAULT_WIDTH
    perimeter = Rectangle.calculate_perimeter(length, width)
    print(perimeter)