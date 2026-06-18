class PositiveChecker:
    def check_positive(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected numeric type, got {type(value).__name__}")
        return value > 0
if __name__ == '__main__':
    checker = PositiveChecker()
    test_values = [42, -5.5, "10", None, True]
    for val in test_values:
        try:
            result = checker.check_positive(val)
            print(f"{val} is {'positive' if result else 'not positive'}")
        except TypeError as e:
            print(f"Error checking {val}: {e}")