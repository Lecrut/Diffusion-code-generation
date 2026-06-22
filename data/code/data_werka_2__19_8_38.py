class ConditionChecker:
    def __init__(self):
        self.ZERO_DIVISION_MESSAGE = "The divisor cannot be zero."

    def check_divisibility(self, dividend, divisor):
        if divisor == 0:
            raise ValueError(self.ZERO_DIVISION_MESSAGE)
        return dividend % divisor == 0

if __name__ == '__main__':
    checker = ConditionChecker()
    num1 = 25
    num2 = 5
    try:
        result = checker.check_divisibility(num1, num2)
        print(f"Is {num1} divisible by {num2}? {result}")
    except ValueError as e:
        print(e)

    num3 = 25
    num4 = 0
    try:
        result = checker.check_divisibility(num3, num4)
        print(f"Is {num3} divisible by {num4}? {result}")
    except ValueError as e:
        print(e)