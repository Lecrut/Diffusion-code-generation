class NumberChecker:
    """A class to check properties of numbers."""

    def check_negativity(self, value):
        """
        Determines if the input value is negative.

        Args:
            value (int or float): The number to check.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Hard-coded sample values for testing without user input or network access
    test_values = [10, -5, 0.0, -3.14, 2, None]

    print("Testing Negative Value Checker:")
    for val in test_values:
        try:
            result = checker.check_negativity(val) if val is not None else "Value cannot be checked"
            status = "Negative" if result else "Non-negative or Invalid Type"
            print(f"{val}: {status}")
        except TypeError as e:
            # Handle cases where type might cause issues, though logic assumes valid numeric input for negative check
            print(f"{val} raised an error (expected behavior): {e}")

    # Additional explicit test with a known positive and negative number to ensure clean execution
    sample_positive = 42
    sample_negative = -99
    assert checker.check_negativity(sample_positive) == False, "Positive check failed"
    assert checker.check_negativity(sample_negative) == True, "Negative check failed"

    print("\nAll assertions passed successfully.")