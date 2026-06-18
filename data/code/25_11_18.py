from typing import Union

class ValueChecker:
    """A utility class to check if a given value is zero."""

    def check_for_zero(self, value: Union[int, float]) -> bool:
        """
        Determines if the input value is equal to zero.

        Args:
            value (int | float): The numeric value to check.

        Returns:
            bool: True if value is 0, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()

    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [
        (5, False),
        (-3.14, False),
        (0, True),
        (float('inf'), False),  # Infinity is not zero
        (float('-inf'), False), # Negative infinity is not zero
    ]

    for value, expected in test_values:
        result = checker.check_for_zero(value)
        assert result == expected, f"Failed for input {value}. Expected {expected}, got {result}"
    
    print("All tests passed.")