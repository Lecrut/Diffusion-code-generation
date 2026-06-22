class ConditionChecker:

    def __init__(self):
        self.ZERO_DIVISION_ERROR_MESSAGE = 'The second number cannot be zero.'

    def check(self, num1, num2):
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError('Both numbers must be integers or floats.')
        try:
            return num1 % num2 == 0
        except ZeroDivisionError:
            raise ValueError(self.ZERO_DIVISION_ERROR_MESSAGE)
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check(20, 5))
    print(checker.check(20, 7))
    try:
        print(checker.check(20, 0))
    except ValueError as e:
        print(e)