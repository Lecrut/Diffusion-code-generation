class GeometryCalculator:
    @staticmethod
    def calculate_perimeter(length, width):
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative")
        return 2 * (length + width)

if __name__ == '__main__':
    try:
        rectangle_length = 8
        rectangle_width = 5
        perimeter = GeometryCalculator.calculate_perimeter(rectangle_length, rectangle_width)
        print(perimeter)
    except ValueError as e:
        print(e)