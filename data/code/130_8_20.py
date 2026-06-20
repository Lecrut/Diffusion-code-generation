class ZeroChecker:
    @staticmethod
    def is_zero(value):
        return value == 0

if __name__ == '__main__':
    print(ZeroChecker.is_zero(1))
    print(ZeroChecker.is_zero(-1))
    print(ZeroChecker.is_zero(0))
    print(ZeroChecker.is_zero(0.0))
    print(ZeroChecker.is_zero("0"))
    print(ZeroChecker.is_zero(5))