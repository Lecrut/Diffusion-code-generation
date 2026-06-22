class ConditionChecker:

    def __init__(self):
        self.ZERO_DIVISION_ERROR_MESSAGE = 'The second number cannot be zero.'

    def validate_inputs(self, num1, num2):
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError('Both numbers must be integers or floats.')
        if num2 == 0:
            raise ValueError(self.ZERO_DIVISION_ERROR_MESSAGE)

    def check(self, num1, num2):
        self.validate_inputs(num1, num2)
        return num1 % num2 == 0
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check(30, 5))
    print(checker.check(30, 7))
    try:
        print(checker.check(30, 0))
    except ValueError as e:
        print(e)