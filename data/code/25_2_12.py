class ValueChecker:
    """A class designed to check if a given value is zero."""

    def check_if_zero(self, value):
        """
        Determines if the input value is equal to zero.

        Args:
            value (int or float): The numeric value to be checked.

        Returns:
            bool: True if the value is zero, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    
    # Hard-coded sample values for testing without user input or network access
    test_values = [
        (0, "zero integer"),
        (-5, "negative number"),
        (3.14, "positive float"),
        (0.0, "zero as float"),
        ("string", "non-numeric string - will raise TypeError on comparison in Python 2/3 depending on context but here treated generically"),
    ]

    for value, description in test_values:
        try:
            is_zero = checker.check_if_zero(value)
            print(f"Value {description} ({value}): {'Zero' if is_zero else 'Not Zero'}")
        except Exception as e:
            # Handle cases where non-numeric types are passed (though the task implies numeric check primarily)
            print(f"Error checking {description}: {e}")

    # Explicit test with integer zero to ensure clarity
    assert checker.check_if_zero(0), "Should return True for 0"
    assert not checker.check_if_zero(-1), "Should return False for -1"
    assert not checker.check_if_zero(42), "Should return False for 42"

    print("All assertions passed.")