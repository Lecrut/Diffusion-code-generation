class TrianglePerimeterCalculator:
    MIN_SIDE_LENGTH = 0.1

    @staticmethod
    def validate_side_length(side):
        if not isinstance(side, (int, float)) or side <= TrianglePerimeterCalculator.MIN_SIDE_LENGTH:
            raise ValueError("All sides must be positive numbers greater than zero")

    @staticmethod
    def calculate_triangle_perimeter(a, b, c):
        TrianglePerimeterCalculator.validate_side_length(a)
        TrianglePerimeterCalculator.validate_side_length(b)
        TrianglePerimeterCalculator.validate_side_length(c)
        return a + b + c

if __name__ == '__main__':
    try:
        perimeter = TrianglePerimeterCalculator.calculate_triangle_perimeter(4.5, 6.3, 7.8)
        print(perimeter)
    except ValueError as e:
        print(e)