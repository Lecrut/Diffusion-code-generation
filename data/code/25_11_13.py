from typing import Any

class ValueChecker:
    """A utility class to check if a given value is zero."""

    def check_for_zero(self, value: Any) -> bool:
        """
        Determines if the input 'value' is equal to zero.

        Args:
            value (Any): The value to be checked for equality with zero.

        Returns:
            bool: True if value is 0 or equivalent to 0 in numeric types, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()

    # Sample values to test without user input
    test_cases = [
        0,
        -123456789,
        0.0,
        float('inf'),
        float('-inf'),
        "0",       # String zero (should be False as per strict equality)
        [],        # Empty list
        {},        # Empty dict
    ]

    print("Testing ValueChecker.check_for_zero()")
    for value in test_cases:
        result = checker.check_for_zero(value)
        status = "is" if result else "is not"
        print(f"{value!r} {status} equal to zero.")