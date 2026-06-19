class ConditionChecker:

    def check(self, dividend, divisor):
        try:
            return dividend % divisor == 0
        except ZeroDivisionError:
            return False
if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check(10, 2)
    print(result)
    result = checker.check(10, 0)
    print(result)