class ZeroChecker:
    ZERO_VALUES = {0, 0.0}

    @staticmethod
    def is_zero(value):
        return value in ZeroChecker.ZERO_VALUES

if __name__ == '__main__':
    print(ZeroChecker.is_zero(0))
    print(ZeroChecker.is_zero(0.0))
    print(ZeroChecker.is_zero(-0))
    print(ZeroChecker.is_zero(-0.0))
    print(ZeroChecker.is_zero(1))
    print(ZeroChecker.is_zero(1.0))