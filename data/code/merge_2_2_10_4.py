class PositiveChecker:
    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a numeric type.")
        return value > 0
if __name__ == '__main__':
    checker = PositiveChecker()
    test_values = [10, -5.5, "invalid", True]
    for val in test_values:
        try:
            result = checker.validate(val)
            print(f"{val} is positive: {result}")
        except TypeError as e:
            print(f"Error validating {val}: {e}")