"""Utility module for checking negativity in numerical values."""

class NegativityChecker:
    """A utility class to check if a number is negative."""

    @staticmethod
    def is_negative(value):
        """Check if the provided value is strictly less than zero.

        Args:
            value (int | float): The numeric value to evaluate.

        Returns:
            bool: True if value < 0, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_values = [
        -5,
        0,
        3.14,
        -2.718,
        float('-inf'),
        float('inf')
    ]

    print("Testing NegativityChecker.is_negative():")
    for val in test_values:
        result = NegativityChecker.is_negative(val)
        status = "Negative" if result else "Non-negative (zero or positive)"
        print(f"{val}: {status}")