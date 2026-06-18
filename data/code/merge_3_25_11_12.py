from typing import Any

class ValueChecker:
    """A class to check if a given value is equal to zero."""

    def check_for_zero(self, value: Any) -> bool:
        """
        Determines if the input 'value' is numerically equal to zero.

        This method handles integers and floats by comparing them directly with 0.
        For other types (like strings), it returns False unless an explicit 
        conversion logic was intended, but based on standard numeric comparison,
        non-numeric values are not considered zero in this context.

        Args:
            value (Any): The input value to check. Can be int or float.

        Returns:
            bool: True if the value is numerically equal to 0, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()

    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [
        (0, True),           # Integer zero
        (-0, True),          # Negative integer zero (equivalent to 0)
        (1.5, False),        # Float non-zero
        (0.0, True),         # Explicit float zero
        ("zero", False),     # String "zero" is not numerically zero here
    ]

    for value, expected in test_values:
        result = checker.check_for_zero(value)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: check_for_zero({value!r}) -> {result} (expected {expected})")