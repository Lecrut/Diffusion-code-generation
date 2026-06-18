class NumberChecker:
    def check_positivity(self, value):
        """Check if a numeric input is strictly positive."""
        return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values for testing without user interaction or external dependencies
    test_values = [5.5, -3, 0, "10", True]
    
    results = []
    for val in test_values:
        is_positive = checker.check_positivity(val)
        print(f"Value {val} ({type(val).__name__}): Is positive? {is_positive}")