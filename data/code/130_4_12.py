class ZeroChecker:
    ZERO = 0

    @staticmethod
    def is_zero(value):
        return value == ZeroChecker.ZERO

if __name__ == '__main__':
    test_values = [0, 1, -2, 3.14, 0j]
    for val in test_values:
        print(ZeroChecker.is_zero(val))