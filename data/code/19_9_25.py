class ConditionChecker:

    def check(self, numerator, denominator):
        try:
            return numerator % denominator == 0
        except ZeroDivisionError:
            return False
if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check(10, 2)
    print(result)
    result = checker.check(10, 0)
    print(result)
    result = checker.check(15, 3)
    print(result)
    result = checker.check(7, 3)
    print(result)