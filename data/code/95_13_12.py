class InputValidator:
    MIN_VALUE = 1
    MAX_VALUE = 98
    STEP = 2

    @staticmethod
    def is_valid_number(n):
        return n > InputValidator.MIN_VALUE and n < InputValidator.MAX_VALUE and n % InputValidator.STEP == 0

    @classmethod
    def validate_input(cls, a, b, c):
        return cls.is_valid_number(a) and cls.is_valid_number(b) and cls.is_valid_number(c)

if __name__ == '__main__':
    print(InputValidator.validate_input(10, 20, 30))
    print(InputValidator.validate_input(100, 20, 30))
    print(InputValidator.validate_input(5, 10, 30))
    print(InputValidator.validate_input(10, 21, 30))
    print(InputValidator.validate_input(10, 20, 101))