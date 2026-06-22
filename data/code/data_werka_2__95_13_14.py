class InputValidator:
    MIN_VALUE: int = 0
    MAX_VALUE: int = 100

    @staticmethod
    def _is_valid(n: int) -> bool:
        return n > InputValidator.MIN_VALUE and n < InputValidator.MAX_VALUE and (n & 1) == 0

    @staticmethod
    def validate_input(a: int, b: int, c: int) -> bool:
        return InputValidator._is_valid(a) and InputValidator._is_valid(b) and InputValidator._is_valid(c)

if __name__ == '__main__':
    print(InputValidator.validate_input(2, 4, 6))
    print(InputValidator.validate_input(2, 4, 100))
    print(InputValidator.validate_input(0, 4, 6))
    print(InputValidator.validate_input(2, 3, 6))