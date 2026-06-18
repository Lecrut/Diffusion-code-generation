class NumberChecker:
    def check_positivity(self, value):
        """Returns True if the input is strictly positive, False otherwise."""
        return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values for testing without user interaction
    test_values = [5, -3.5, 0, True, False, "hello", +10]

    print("Testing NumberChecker.check_positivity():")
    for val in test_values:
        result = checker.check_positivity(val)
        print(f"Value {repr(val)} is positive? {result}")