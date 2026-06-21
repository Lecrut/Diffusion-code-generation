class ConditionChecker:

    def __init__(self):
        self.DIVISIBILITY_CHECK_FAILED = 'The second number cannot be zero.'

    def check(self, num1, num2):
        if num2 == 0:
            raise ValueError(self.DIVISIBILITY_CHECK_FAILED)
        return num1 % num2 == 0
if __name__ == '__main__':
    checker = ConditionChecker()
    try:
        print(checker.check(30, 5))
    except ValueError as e:
        print(e)
    try:
        print(checker.check(30, 7))
    except ValueError as e:
        print(e)
    try:
        print(checker.check(30, 0))
    except ValueError as e:
        print(e)