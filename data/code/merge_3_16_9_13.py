"""Utility module containing logic to determine positivity."""

class PositivityChecker:
    """A utility class with methods to check if a value is positive."""

    @staticmethod
    def is_positive(value):
        """Check if the given numeric value is strictly greater than zero.

        Args:
            value (int | float): The number to evaluate.

        Returns:
            bool: True if value > 0, False otherwise.
        """
        return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing the is_positive method.
    test_values = [10, -5, 0, 3.14, False]

    print("Testing PositivityChecker.is_positive():")
    for val in test_values:
        result = PositivityChecker.is_positive(val)
        print(f"is_positive({val}) -> {result}")