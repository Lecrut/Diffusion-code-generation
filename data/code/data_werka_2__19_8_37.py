class ConditionChecker:
    DIVISION_BY_ZERO_ERROR = 'The second number cannot be zero.'

    def check(self, num1, num2):
        if num2 == 0:
            raise ValueError(self.DIVISION_BY_ZERO_ERROR)
        return num1 % num2 == 0
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check(25, 5))
    print(checker.check(25, 4))
    try:
        print(checker.check(25, 0))
    except ValueError as e:
        print(e)