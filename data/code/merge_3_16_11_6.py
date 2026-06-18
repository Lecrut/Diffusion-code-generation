class NumberChecker:
    """A utility class to check properties of numeric values."""

    def check_positivity(self, value):
        """
        Determines if the provided value is strictly positive.

        Args:
            value (int or float): The number to be checked.

        Returns:
            bool: True if the value is greater than zero, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values for testing without user input or files
    test_values = [10, -5, 0.0, 3.14, float('-inf'), float('inf')]

    print("Testing positivity check:\n")
    results = []
    for val in test_values:
        is_positive = checker.check_positivity(val)
        status = "Positive" if is_positive else "Non-positive (zero or negative)"
        results.append(status)
        print(f"{val} ({type(val).__name__}): {status}")

    # Verify the expected outcomes for known values to ensure correctness logic
    assert checker.check_positivity(10), "Failed: 10 should be positive"
    assert not checker.check_positivity(-5), "Failed: -5 should not be positive"
    assert not checker.check_positivity(0.0), "Failed: 0 should not be positive"
    print("\nAll assertions passed.")