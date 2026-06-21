class NumberChecker:
    def check_positivity(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be an integer or a float.")
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [10, -5, 0, 3.5, -2.3, 'a', None]
    for value in sample_values:
        try:
            result = checker.check_positivity(value)
            print(f"Is {value} positive? {result}")
        except ValueError as e:
            print(f"Error checking {value}: {e}")