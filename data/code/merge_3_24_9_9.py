from typing import Any

class MathUtils:
    """Utility class containing mathematical helper functions."""

    @staticmethod
    def is_negative(value: float) -> bool:
        """Check if a given value is strictly negative.

        Args:
            value (float): The number to check.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [5, -3.14, 0, -0.001, float('inf'), float('-inf')]

    print("Testing negativity check:")
    for val in test_values:
        result = MathUtils.is_negative(val)
        status = "Negative" if result else "Non-negative or infinity"
        print(f"{val} -> {status}")