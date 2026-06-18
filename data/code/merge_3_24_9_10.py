import math

class NegativityUtils:
    """Utility class containing methods to check negativity."""

    @staticmethod
    def is_negative(value):
        """
        Check if a number is negative.

        Args:
            value (int or float): The numerical value to evaluate.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_values = [-5, -0.1, 0, 3.14]

    print("Testing negativity check:")
    for val in test_values:
        result = NegativityUtils.is_negative(val)
        status = "Negative" if result else "Non-negative"
        print(f"{val} is {status}")