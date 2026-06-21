class Rectangle:
    DEFAULT_LENGTH = 6
    DEFAULT_WIDTH = 2

    @staticmethod
    def calculate_perimeter(length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return 2 * (length + width)

if __name__ == '__main__':
    length = Rectangle.DEFAULT_LENGTH
    width = Rectangle.DEFAULT_WIDTH
    print(Rectangle.calculate_perimeter(length, width))