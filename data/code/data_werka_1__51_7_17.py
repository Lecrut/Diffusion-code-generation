class GeometryCalculator:
    TWO = 2

    @staticmethod
    def calculate_perimeter(length, width):
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative")
        return GeometryCalculator.TWO * (length + width)

if __name__ == '__main__':
    rectangle_length = 8
    rectangle_width = 2
    perimeter = GeometryCalculator.calculate_perimeter(rectangle_length, rectangle_width)
    print(perimeter)