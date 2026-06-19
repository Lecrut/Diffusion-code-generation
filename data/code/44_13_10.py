class Rectangle:
    DEFAULT_LENGTH = 8
    DEFAULT_WIDTH = 4

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    length_val = 10
    width_val = 5
    perimeter = Rectangle.calculate_perimeter(length_val, width_val)
    print(perimeter)