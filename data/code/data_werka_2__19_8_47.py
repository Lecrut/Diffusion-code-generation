class ConditionChecker:

    def check(self, num1, num2):
        if num2 == 0:
            raise ValueError('Division by zero is not allowed.')
        return num1 % num2 == 0
if __name__ == '__main__':
    checker = ConditionChecker()
    numerator = 25
    denominator = 5
    try:
        result = checker.check(numerator, denominator)
        print(f'Is {numerator} divisible by {denominator}? {result}')
    except ValueError as e:
        print(e)
    numerator = 30
    denominator = 4
    try:
        result = checker.check(numerator, denominator)
        print(f'Is {numerator} divisible by {denominator}? {result}')
    except ValueError as e:
        print(e)
    numerator = 10
    denominator = 0
    try:
        result = checker.check(numerator, denominator)
        print(f'Is {numerator} divisible by {denominator}? {result}')
    except ValueError as e:
        print(e)