class GeometryCalculator:
    @staticmethod
    def validate_dimensions(length, width):
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError("Length and width must be numbers")
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative")

    @staticmethod
    def calculate_perimeter(length, width):
        GeometryCalculator.validate_dimensions(length, width)
        return 2 * (length + width)

if __name__ == '__main__':
    rectangle_length = 8
    rectangle_width = 5
    perimeter = GeometryCalculator.calculate_perimeter(rectangle_length, rectangle_width)
    print(perimeter)