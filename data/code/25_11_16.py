from typing import Any

class ValueChecker:
    """A utility class to check if a given value is zero."""

    def check_for_zero(self, value: Any) -> bool:
        """
        Determines if the input 'value' is equal to zero.

        Args:
            value (Any): The value to be checked for equality with zero.

        Returns:
            bool: True if the value is numerically equivalent to 0, False otherwise.
                  Handles integers and floats correctly while ignoring non-numeric types.
        """
        try:
            return float(value) == 0.0
        except (TypeError, ValueError):
            # If conversion fails, it's not zero by definition in this context
            return False

if __name__ == '__main__':
    checker = ValueChecker()

    test_cases = [
        ("Zero integer", 0),
        ("Negative one", -1),
        ("Positive two", 2.5),
        ("String zero", "0"),
        ("Empty string", ""),
        ("None value", None),
        ("Float point", 0.0),
    ]

    for description, test_value in test_cases:
        result = checker.check_for_zero(test_value)
        print(f"{description}: {test_value} -> Is zero? {result}")