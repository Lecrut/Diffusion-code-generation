class NumberChecker:
    def is_zero(self, number):
        return number == 0

if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.is_zero(0))
    print(checker.is_zero(0.0))
    print(checker.is_zero(1))
    print(checker.is_zero(-1))
    print(checker.is_zero(3.14))