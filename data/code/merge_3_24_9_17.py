"""Utility module containing logic to check if a number is negative."""

class NegativeCheckUtils:
    """A utility class providing methods to analyze numeric values regarding negativity."""

    @staticmethod
    def is_negative(value):
        """
        Check if the given value is strictly less than zero.

        Args:
            value (int | float): The number to evaluate for negativity.

        Returns:
            bool: True if the value is negative, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_values = [
        -5,
        0,
        3.14,
        -2.718,
        float('inf'),
        float('-inf')
    ]

    print("Testing NegativeCheckUtils.is_negative():")
    for val in test_values:
        result = NegativeCheckUtils.is_negative(val)
        status = "Negative" if result else "Non-negative (includes zero)"
        # Note: Infinity values are treated as non-negative by standard comparison rules.
        print(f"{val!r} -> {status}")