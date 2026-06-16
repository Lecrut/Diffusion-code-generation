class PositiveChecker:
    def check(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a numeric type.")
        return value > 0
if __name__ == '__main__':
    checker = PositiveChecker()
    test_values = [42, -5.5, "10", True]
    for val in test_values:
        try:
            result = checker.check(val)
            print(f"{val} is {'positive' if result else 'not positive'}")
        except TypeError as e:
            print(f"Error with {type(val).__name__}: {e}")