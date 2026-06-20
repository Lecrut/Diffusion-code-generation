class ZeroChecker:
    ZERO = 0

    @staticmethod
    def is_zero(value):
        return value == ZeroChecker.ZERO

if __name__ == '__main__':
    print(ZeroChecker.is_zero(0))
    print(ZeroChecker.is_zero(42))
    print(ZeroChecker.is_zero(-1))
    print(ZeroChecker.is_zero(3.14))