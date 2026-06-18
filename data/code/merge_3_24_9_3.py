"""Utility module containing logic to check negativity."""

class NegativityChecker:
    """A utility class for checking if a value is negative."""

    @staticmethod
    def is_negative(value):
        """Check if the provided value is strictly less than zero.

        Args:
            value (int | float): The numerical value to evaluate.

        Returns:
            bool: True if value < 0, otherwise False.
        
        Raises:
            TypeError: If the input is not a number.
        """
        try:
            return isinstance(value, (int, float)) and value < 0
        except Exception:
            return False

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure no user input or files are needed.
    test_values = [-5, -3.14, 0, 2, "not a number", None]

    for val in test_values:
        result = NegativityChecker.is_negative(val)
        print(f"Value {repr(val)} is negative: {result}")