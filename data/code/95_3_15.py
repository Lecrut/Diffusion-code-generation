class RangeValidator:
    MIN_VALUE = 0
    MAX_VALUE = 100
    PARITY = 2

    @staticmethod
    def check(n):
        return n > RangeValidator.MIN_VALUE and n % RangeValidator.PARITY == 0 and n < RangeValidator.MAX_VALUE

if __name__ == '__main__':
    result = RangeValidator.check(42)
    print(result)