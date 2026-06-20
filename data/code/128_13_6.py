class NumberChecker:
    def is_negative(self, num):
        return num < 0

if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.is_negative(-5))
    print(checker.is_negative(3))
    print(checker.is_negative(0))
    print(checker.is_negative(-1.5))