class IntegerSubtractor:
    MIN_INT = -2147483648
    MAX_INT = 2147483647

    @staticmethod
    def is_valid_integer(value):
        return isinstance(value, int) and IntegerSubtractor.MIN_INT <= value <= IntegerSubtractor.MAX_INT

    @staticmethod
    def subtract_integers(a: int, b: int) -> int:
        if not IntegerSubtractor.is_valid_integer(a) or not IntegerSubtractor.is_valid_integer(b):
            raise ValueError('Both inputs must be integers within the valid range')
        return a - b
if __name__ == '__main__':
    result = IntegerSubtractor.subtract_integers(10, 5)
    print(result)