class ValueChecker:

    def check_if_zero(self, value):
        return value == 0
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.check_if_zero(0))
    print(checker.check_if_zero(1))
    print(checker.check_if_zero(-1))
    print(checker.check_if_zero(0.0))