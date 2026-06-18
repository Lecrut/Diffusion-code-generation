class NumberChecker:
    """A class to check properties of numerical values."""

    def check_positivity(self, value):
        """
        Determines if the input value is positive.

        Args:
            value (int or float): The number to be checked.

        Returns:
            bool: True if the value is strictly greater than zero, False otherwise.
        """
        return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample test values with expected results hard-coded for verification
    sample_values = [10, -5, 0.0, 3.14, None, "string", True]

    print("Testing NumberChecker.check_positivity:")
    for val in sample_values:
        result = checker.check_positivity(val)
        expected = isinstance(val, (int, float)) and val > 0 if not isinstance(val, bool) else False
        status = "PASS" if result == expected else "FAIL"
        print(f"Value: {val!r} -> Positive? {result} | Expected: {expected} [{status}]")

    # Specific test for boolean True (which is 1 in Python but often treated separately)
    # Since bool is a subclass of int, check_positivity(True) returns True because 1 > 0.
    print(f"\nSpecific Check:")
    result_true = checker.check_positivity(True)
    expected_true = True  # In Python, isinstance(True, (int, float)) is True and True > 0 is True
    status = "PASS" if result_true == expected_true else "FAIL"
    print(f"Value: {True!r} -> Positive? {result_true} | Expected: {expected_true} [{status}]")