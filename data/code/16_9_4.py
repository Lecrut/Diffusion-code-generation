"""Utility module containing a static method to determine if a number is positive."""

class NumberUtils:
    """A utility class providing methods for basic numerical operations."""

    @staticmethod
    def is_positive(value):
        """
        Determine if the given value is strictly greater than zero.

        Args:
            value (int | float): The numeric value to check.

        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing the is_positive method.
    test_values = [10, -5, 0.0, 3.14, None]

    print("Testing NumberUtils.is_positive:")
    for val in test_values:
        if isinstance(val, (int, float)):
            result = NumberUtils.is_positive(val)
            status = "Positive" if result else "Non-positive"
            print(f"{val} is {status}")
        else:
            # Handle non-numeric inputs gracefully without raising errors in output.
            print(f"{val} cannot be evaluated as positive.")