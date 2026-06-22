class Rectangle:
    @staticmethod
    def validate_dimensions(length, width):
        if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
            raise ValueError("Dimensions must be numbers")
        if length <= 0 or width <= 0:
            raise ValueError("Dimensions must be positive")

    @staticmethod
    def area():
        Rectangle.validate_dimensions(5, 3)
        return 5 * 3

if __name__ == '__main__':
    print(Rectangle.area())