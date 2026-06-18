from typing import Any

class ValueChecker:
    """A utility class to check if a given value is zero."""

    def check_for_zero(self, value: Any) -> bool:
        """
        Determines if the input value is equal to zero.

        Args:
            value (Any): The value to be checked. This can be an integer or float.

        Returns:
            bool: True if the value is exactly 0, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()

    # Hard-coded sample values to test without user input
    samples = [0, -1, 1, 0.0, -0.0, float('inf'), "0", None]

    for item in samples:
        result = checker.check_for_zero(item)
        print(f"Value {item!r}: is zero? {result}")