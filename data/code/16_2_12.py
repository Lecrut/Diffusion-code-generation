class NumberChecker:
    """A class to perform basic numerical validations."""

    def check_positivity(self, value):
        """Determines if the input value is positive (greater than zero).
        
        Args:
            value: The number to be checked. Can be an integer or float.
            
        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Hard-coded sample values for testing
    test_values = [10, -5, 0, 3.14]

    print("Number Checker Results:")
    for val in test_values:
        result = checker.check_positivity(val)
        status = "Positive" if result else "Non-positive (zero or negative)"
        print(f"{val}: {status}")