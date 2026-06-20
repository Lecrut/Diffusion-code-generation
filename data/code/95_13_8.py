class InputValidator:
    MIN_VALUE = 1
    MAX_VALUE = 98

    @staticmethod
    def is_positive_even(n):
        return n > 0 and n % 2 == 0

    @classmethod
    def validate_input(cls, a, b, c):
        return all(cls.is_positive_even(x) for x in (a, b, c)) and cls.MIN_VALUE <= a <= cls.MAX_VALUE and cls.MIN_VALUE <= b <= cls.MAX_VALUE and cls.MIN_VALUE <= c <= cls.MAX_VALUE

if __name__ == '__main__':
    print(InputValidator.validate_input(10, 20, 30))
    print(InputValidator.validate_input(100, 20, 30))
    print(InputValidator.validate_input(5, 10, 30))
    print(InputValidator.validate_input(10, 21, 30))
    print(InputValidator.validate_input(10, 20, 101))