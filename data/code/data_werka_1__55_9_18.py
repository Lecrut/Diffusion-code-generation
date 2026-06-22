class Triangle:
    MIN_SIDE_LENGTH = 1

    @staticmethod
    def validate_side_lengths(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Side lengths must be positive numbers.")

    @staticmethod
    def calculate_perimeter(a, b, c):
        Triangle.validate_side_lengths(a, b, c)
        return a + b + c

if __name__ == '__main__':
    try:
        perimeter = Triangle.calculate_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)