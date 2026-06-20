class ZeroChecker:
    def is_zero(self, number):
        return number == 0

if __name__ == '__main__':
    checker = ZeroChecker()
    print(checker.is_zero(0))
    print(checker.is_zero(5))
    print(checker.is_zero(-10))