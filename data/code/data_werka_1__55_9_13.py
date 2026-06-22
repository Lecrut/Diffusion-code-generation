class Triangle:
    MIN_SIDE_LENGTH = 1

    @staticmethod
    def validate_side_length(length):
        if length <= 0:
            raise ValueError("Side lengths must be positive numbers.")

    @classmethod
    def calculate_perimeter(cls, a, b, c):
        cls.validate_side_length(a)
        cls.validate_side_length(b)
        cls.validate_side_length(c)
        return a + b + c

if __name__ == '__main__':
    try:
        perimeter = Triangle.calculate_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)