class TriangleValidator:
    MIN_SIDE = 1
    VALID = True
    INVALID = False

    @staticmethod
    def _check_positive(side):
        return side >= TriangleValidator.MIN_SIDE

    @staticmethod
    def _check_triangle_inequalities(a, b, c):
        return (a + b > c) and (a + c > b) and (b + c > a)

    @classmethod
    def is_valid_triangle(cls, a, b, c):
        if not cls._check_positive(a) or not cls._check_positive(b) or not cls._check_positive(c):
            return cls.INVALID
        return cls.VALID if cls._check_triangle_inequalities(a, b, c) else cls.INVALID

if __name__ == '__main__':
    validator = TriangleValidator()
    print(validator.is_valid_triangle(7, 8, 9))
    print(validator.is_valid_triangle(2, 2, 4))
    print(validator.is_valid_triangle(1, 2, 10))
    print(validator.is_valid_triangle(-5, 5, 5))
    print(validator.is_valid_triangle(0, 3, 4))