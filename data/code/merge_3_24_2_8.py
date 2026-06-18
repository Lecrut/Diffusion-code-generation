class NumberChecker:
    """A class to check properties of numbers."""

    def check_if_negative(self, value):
        """Determines if the input value is negative.

        Args:
            value (int or float): The number to check.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample values for testing without user input or external dependencies
    test_values = [
        -5,      # Negative integer
        10,       # Positive integer
        -3.14,   # Negative float
        0,        # Zero (not negative)
        -0.001,  # Small negative number
        2e-5      # Very small positive number in scientific notation
    ]

    for val in test_values:
        result = checker.check_if_negative(val)
        print(f"Is {val} negative? {result}")