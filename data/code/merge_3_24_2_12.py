class NumberChecker:
    """A class that provides utility methods to check numerical properties."""

    def check_if_negative(self, value):
        """
        Determines if the input value is negative.

        Args:
            value (int or float): The number to be checked.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values for testing
    test_cases = [
        (-5),
        (0),
        (-3.14),
        (100),
        (float('-inf')),
        (float('nan'))  # NaN is neither greater nor less, will return False in standard comparison logic
    ]

    for value in test_cases:
        result = checker.check_if_negative(value)
        print(f"Is {value} negative? {result}")