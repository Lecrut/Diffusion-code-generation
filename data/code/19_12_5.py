class ConditionChecker:
    def check(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a % b == 0
if __name__ == '__main__':
    checker = ConditionChecker()
    result1 = checker.check(10, 2)
    print(f"10 is divisible by 2: {result1}")
    result2 = checker.check(10, 3)
    print(f"10 is divisible by 3: {result2}")
    try:
        checker.check(10, 0)
    except ValueError as e:
        print(f"Error caught for division by zero: {e}")