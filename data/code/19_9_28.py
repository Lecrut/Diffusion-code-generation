class ConditionChecker:

    def check(self, a, b):
        try:
            return a % b == 0
        except ZeroDivisionError:
            return False
if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check(10, 2)
    print(result)