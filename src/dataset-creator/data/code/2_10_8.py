class PositiveChecker:
    def is_positive(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a numeric type.")
        return value > 0
if __name__ == '__main__':
    checker = PositiveChecker()
    test_cases = [42, -5.5, "10", True, None]
    for case in test_cases:
        try:
            result = checker.is_positive(case)
            print(f"{case!r}: {result}")
        except TypeError as e:
            print(f"Error with {case!r}: {e}")