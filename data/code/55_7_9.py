class TriangleCalculator:
    MIN_SIDE_LENGTH = 0.0

    @staticmethod
    def validate_side_length(side):
        if side <= TriangleCalculator.MIN_SIDE_LENGTH:
            raise ValueError("All sides must be positive numbers")

    @staticmethod
    def calculate_triangle_perimeter(a, b, c):
        TriangleCalculator.validate_side_length(a)
        TriangleCalculator.validate_side_length(b)
        TriangleCalculator.validate_side_length(c)
        return a + b + c

if __name__ == '__main__':
    try:
        perimeter = TriangleCalculator.calculate_triangle_perimeter(5, 12, 13)
        print(perimeter)
    except ValueError as e:
        print(e)