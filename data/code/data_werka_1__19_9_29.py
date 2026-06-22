class ConditionChecker:

    def check(self, numerator, denominator):
        try:
            return numerator % denominator == 0
        except ZeroDivisionError:
            return False
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check(10, 2))
    print(checker.check(10, 3))
    print(checker.check(10, 0))