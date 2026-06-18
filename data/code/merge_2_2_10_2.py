class PositiveChecker:
    def is_positive(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a numeric type.")
        return value > 0
if __name__ == '__main__':
    checker = PositiveChecker()
    test_values = [10.5, -3, "42", None]
    for val in test_values:
        try:
            result = checker.is_positive(val)
            print(f"{val}: {result}")
        except TypeError as e:
            print(f"Error with {val}: {e}")