class Rectangle:
    @staticmethod
    def validate_dimensions(length, width):
        if not (isinstance(length, int) and isinstance(width, int)):
            raise ValueError("Both dimensions must be integers.")
        if length <= 0 or width <= 0:
            raise ValueError("Both dimensions must be positive integers.")

    @staticmethod
    def area():
        Rectangle.validate_dimensions(5, 3)
        return 5 * 3

if __name__ == '__main__':
    print(Rectangle.area())