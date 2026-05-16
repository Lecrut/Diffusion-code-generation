class NumberChecker:
    def check_if_negative(self, value):
        return value < 0
if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.check_if_negative(10))
    print(checker.check_if_negative(-5))
    print(checker.check_if_negative(0))
    print(checker.check_if_negative(-100))