from typing import Any

class ValueChecker:
    """A class designed to check if a given value is zero."""

    def check_for_zero(self, value: Any) -> bool:
        """
        Determines if the input value is equal to zero.

        Args:
            value (Any): The numerical or boolean value to check against zero.

        Returns:
            bool: True if value is 0, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    checker = ValueChecker()

    test_values = [0, -1, 1, "", [], {}, None, True, False]

    print("Checking if the following values are zero:")
    for val in test_values:
        result = checker.check_for_zero(val)
        print(f"Value {repr(val)} is zero: {result}")