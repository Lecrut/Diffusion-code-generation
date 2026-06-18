"""Utility module containing a static method to determine if a number is positive."""

class NumberUtilities:
    """A utility class providing methods for basic numerical operations."""

    @staticmethod
    def is_positive(value):
        """Check if the given value is strictly greater than zero.

        Args:
            value (int | float): The numeric value to check.

        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing the is_positive method
    test_values = [10, -5, 0.0, 3.14, -2]

    print("Testing NumberUtilities.is_positive:")
    for val in test_values:
        result = NumberUtilities.is_positive(val)
        status = "Positive" if result else "Non-positive (zero or negative)"
        print(f"{val}: {status}")