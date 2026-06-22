class Rectangle:
    DEFAULT_LENGTH = 5
    DEFAULT_WIDTH = 3

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    length = Rectangle.DEFAULT_LENGTH
    width = Rectangle.DEFAULT_WIDTH
    print(Rectangle.calculate_perimeter(length, width))