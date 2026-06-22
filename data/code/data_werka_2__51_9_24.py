class Rectangle:
    DEFAULT_LENGTH = 5
    DEFAULT_WIDTH = 3

    @staticmethod
    def calculate_perimeter(length=DEFAULT_LENGTH, width=DEFAULT_WIDTH):
        return 2 * (length + width)

if __name__ == '__main__':
    print(Rectangle.calculate_perimeter())