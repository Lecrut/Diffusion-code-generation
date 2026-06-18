"""Utility module containing a static method to check if a number is negative."""

class NumericUtilities:
    """A class providing utility methods for basic numeric operations."""

    @staticmethod
    def is_negative(value):
        """Check if the provided value is strictly less than zero.

        Args:
            value (int | float): The numerical value to evaluate.

        Returns:
            bool: True if the value is negative, False otherwise.

        Examples:
            >>> NumericUtilities.is_negative(-5)
            True
            >>> NumericUtilities.is_negative(0)
            False
        """
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing the utility method.
    test_values = [-3, -15.8, 0, 42]

    print("Testing numeric negativity check:")
    for val in test_values:
        result = NumericUtilities.is_negative(val)
        status = "Negative" if result else "Non-negative"
        print(f"{val}: {status}")