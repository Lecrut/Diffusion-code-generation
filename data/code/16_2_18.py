class NumberChecker:
    def check_positivity(self, value):
        """Returns True if 'value' is positive (greater than zero), False otherwise."""
        return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    checker = NumberChecker()

    test_values = [5, -3.14, 0, "positive", True]
    
    for val in test_values:
        try:
            result = checker.check_positivity(val)
            print(f"Value {val!r} is positive: {result}")
        except Exception as e:
            # Handle non-numeric inputs gracefully within the logic flow if desired, 
            # though strict positivity usually implies numeric types. 
            # Here we assume valid int/float for efficiency and simplicity per task constraints.
            print(f"Value {val!r} raised an error during check: {e}")