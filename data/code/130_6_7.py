class ZeroChecker:
    ZERO = 0

    @staticmethod
    def is_zero(number):
        return number == ZeroChecker.ZERO

if __name__ == '__main__':
    print(ZeroChecker.is_zero(0))
    print(ZeroChecker.is_zero(1))