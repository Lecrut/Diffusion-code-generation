class Triangle:
    MIN_SIDE_LENGTH = 0

    @staticmethod
    def validate_side_lengths(a, b, c):
        if not all(isinstance(x, (int, float)) and x > Triangle.MIN_SIDE_LENGTH for x in [a, b, c]):
            raise ValueError("Side lengths must be positive numbers.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("The given side lengths do not form a valid triangle.")

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