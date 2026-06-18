class NumberChecker:
    def check_negativity(self, value):
        """Returns True if the input is negative, False otherwise."""
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    test_cases = [10, -5.5, 0, None]

    for val in test_cases:
        result = checker.check_negativity(val)
        print(f"Is {val} negative? {result}")