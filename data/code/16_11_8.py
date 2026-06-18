class NumberChecker:
    """A class to check properties of numbers."""

    def check_positivity(self, value):
        """
        Determines if the provided numeric value is positive.

        Args:
            value (int or float): The number to check.

        Returns:
            bool: True if the value is strictly greater than zero, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [5, -3, 0, 2.5, -10.7]

    print("Testing positivity check:")
    for val in test_values:
        result = checker.check_positivity(val)
        status = "Positive" if result else "Non-positive (zero or negative)"
        print(f"{val}: {status}")