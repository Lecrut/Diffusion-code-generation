class TriangleValidator:
    MIN_SIDE = 1

    @staticmethod
    def validate(a, b, c):
        if not TriangleValidator._check_positive(a) or not TriangleValidator._check_positive(b) or not TriangleValidator._check_positive(c):
            return False
        if not TriangleValidator._check_sum(a, b, c):
            return False
        return True

    @staticmethod
    def _check_positive(length):
        return length >= TriangleValidator.MIN_SIDE

    @staticmethod
    def _check_sum(a, b, c):
        return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    validator = TriangleValidator()
    print(validator.validate(3, 4, 5))
    print(validator.validate(1, 2, 3))
    print(validator.validate(-1, 2, 3))
    print(validator.validate(0, 5, 5))
    print(validator.validate(7, 10, 5))