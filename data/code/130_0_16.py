class ZeroChecker:
    def is_zero(self, number):
        return abs(number) < 1e-9

if __name__ == '__main__':
    checker = ZeroChecker()
    print(checker.is_zero(0))
    print(checker.is_zero(5))
    print(checker.is_zero(-0))
    print(checker.is_zero(3.14))