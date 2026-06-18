class NumberChecker:
    """A class to check properties of numbers."""

    def check_if_negative(self, value):
        """Determines if the input value is negative.

        Args:
            value (int or float): The number to be checked.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample values for testing without user input or external dependencies
    test_values = [
        -5,      # Negative integer
        0,       # Zero (not negative)
        3.14,    # Positive float
        -2.7e-3, # Small negative number in scientific notation
    ]

    for val in test_values:
        result = checker.check_if_negative(val)
        print(f"Is {val} negative? {result}")