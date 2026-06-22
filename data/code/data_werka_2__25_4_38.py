class ZeroChecker:
    TOLERANCE = 1e-09

    @staticmethod
    def is_zero(x):
        return abs(x) < ZeroChecker.TOLERANCE

if __name__ == '__main__':
    print(ZeroChecker.is_zero(0))
    print(ZeroChecker.is_zero(-0.0))
    print(ZeroChecker.is_zero(1e-10))
    print(ZeroChecker.is_zero(1e-08))
    print(ZeroChecker.is_zero(123456789))
    print(ZeroChecker.is_zero(1))