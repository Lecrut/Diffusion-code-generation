class ZeroChecker:
    ZERO = 0

    @staticmethod
    def is_zero(num):
        return num == ZeroChecker.ZERO

if __name__ == '__main__':
    checker = ZeroChecker()
    print(checker.is_zero(0))
    print(checker.is_zero(42))