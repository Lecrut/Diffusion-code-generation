class NumberChecker:
    """A class to check properties of numbers."""

    def check_positivity(self, value):
        """
        Determines if the input value is positive.

        A number is considered positive if it is strictly greater than zero.

        Args:
            value (int | float): The numerical value to evaluate.

        Returns:
            bool: True if 'value' > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample values with varying types and signs
    test_values = [5, -3, 0.1, 0, "abc", True]

    for val in test_values:
        try:
            is_positive = checker.check_positivity(val)
            print(f"Value {val!r} is positive: {is_positive}")
        except TypeError as e:
            # Handle non-numeric inputs gracefully without breaking the script
            print(f"Error checking value {val!r}: {e}")