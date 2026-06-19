class ConditionChecker:

    def check(self, num1, num2):
        try:
            return num1 % num2 == 0
        except ZeroDivisionError:
            return False
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check(10, 2))
    print(checker.check(10, 0))