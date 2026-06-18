"""Utility module containing logic to check if a number is negative."""

class NumberUtilities:
    """A utility class providing methods for basic numeric checks."""

    @staticmethod
    def is_negative(value):
        """Check if the given value is strictly less than zero.

        Args:
            value (int | float): The numerical value to evaluate.

        Returns:
            bool: True if value < 0, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files.
    test_values = [-5, -3.14, 0, 2, 10]

    print("Testing negativity check:")
    for val in test_values:
        result = NumberUtilities.is_negative(val)
        status = "Negative" if result else "Non-negative (zero or positive)"
        print(f"{val}: {status}")