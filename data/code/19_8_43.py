class ConditionChecker:

    def __init__(self):
        self.DIVISION_BY_ZERO_MSG = 'The second number cannot be zero.'

    def check(self, num1, num2):
        if num2 == 0:
            raise ValueError(self.DIVISION_BY_ZERO_MSG)
        return num1 % num2 == 0
if __name__ == '__main__':
    checker = ConditionChecker()
    try:
        print(checker.check(30, 5))
        print(checker.check(30, 7))
        print(checker.check(30, 0))
    except ValueError as e:
        print(e)