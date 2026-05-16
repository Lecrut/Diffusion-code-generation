class ConditionChecker:
    def check(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a % b == 0
if __name__ == '__main__':
    checker = ConditionChecker()
    num1 = 10
    num2 = 2
    result1 = checker.check(num1, num2)
    print(f"Is {num1} divisible by {num2}? {result1}")
    num1 = 10
    num2 = 3
    result2 = checker.check(num1, num2)
    print(f"Is {num1} divisible by {num2}? {result2}")
    num1 = 10
    num2 = 0
    try:
        result3 = checker.check(num1, num2)
        print(f"Is {num1} divisible by {num2}? {result3}")
    except ValueError as e:
        print(f"Error encountered: {e}")