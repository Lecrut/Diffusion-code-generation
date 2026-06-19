class ConditionChecker:

    def check(self, numerator, denominator):
        try:
            return numerator % denominator == 0
        except ZeroDivisionError:
            return False
if __name__ == '__main__':
    checker = ConditionChecker()
    result1 = checker.check(10, 2)
    result2 = checker.check(10, 0)
    print(result1)
    print(result2)