class ConditionChecker:
    DIVISION_BY_ZERO_ERROR_MESSAGE = 'The second number cannot be zero.'

    def check(self, num1, num2):
        if self._is_zero(num2):
            raise ValueError(self.DIVISION_BY_ZERO_ERROR_MESSAGE)
        return num1 % num2 == 0

    @staticmethod
    def _is_zero(number):
        return number == 0

if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check(25, 5)
    print(result)
    result = checker.check(25, 4)
    print(result)
    try:
        result = checker.check(25, 0)
        print(result)
    except ValueError as e:
        print(e)