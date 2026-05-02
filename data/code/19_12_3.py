class ConditionChecker:
    def check(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a % b == 0
if __name__ == '__main__':
    checker = ConditionChecker()
    result1 = checker.check(10, 2)
    print(f"10 is divisible by 2: {result1}")
    result2 = checker.check(10, 3)
    print(f"10 is divisible by 3: {result2}")
    try:
        result3 = checker.check(10, 0)
        print(f"10 is divisible by 0: {result3}")
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")