class ValueChecker:
    """A class that provides utility methods to check properties of various values."""

    def check_if_zero(self, value):
        """Determines if the input value is zero or equivalent to zero (e.g., 0.0)."""
        return bool(value == 0)

if __name__ == '__main__':
    checker = ValueChecker()

    # Hard-coded sample values for testing without user interaction
    test_values = [
        0,           # Integer zero - should be True
        0.0,          # Float zero - should be True
        "0",          # String representation of zero (treated as non-zero by ==) -> False
        [],           # Empty list - treated as falsy but not equal to int/float 0? 
                     # In Python [] != 0 is True. However, the task asks specifically for 'zero'.
                     # Strictly speaking, only numeric zero should match unless specified otherwise.
                     # Let's stick to strict equality: bool(value == 0) returns False for [].
        "",           # Empty string - not equal to int/float 0 -> False
    ]

    print("Value Checker Test Results:")
    for val in test_values:
        result = checker.check_if_zero(val)
        status = "IS ZERO" if result else "NOT ZERO"
        print(f"{repr(val):15} -> {status}")