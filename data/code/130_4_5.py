class ZeroChecker:
    def is_zero(self, value):
        return value == 0

if __name__ == '__main__':
    checker = ZeroChecker()
    print(checker.is_zero(0))
    print(checker.is_zero(1))
    print(checker.is_zero(-3))
    print(checker.is_zero(0.0))