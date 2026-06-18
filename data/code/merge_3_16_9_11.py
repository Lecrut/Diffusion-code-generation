"""Utility module containing logic to determine positivity."""

class PositivityChecker:
    """A utility class for checking if a value is positive."""

    @staticmethod
    def is_positive(value):
        """Check if a given numeric value is strictly greater than zero.

        Args:
            value (int | float): The number to evaluate.

        Returns:
            bool: True if the value is positive, False otherwise.
        """
        return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_cases = [
        -5,
        0,
        3.14,
        "negative_string",  # This will be handled gracefully by isinstance check before comparison.
    ]

    print("Testing PositivityChecker.is_positive():")
    for case in test_cases:
        try:
            result = PositivityChecker.is_positive(case)
            status = "Positive" if result else "Not Positive or Invalid Type"
            print(f"{case!r}: {status}")
        except Exception as e:  # Should not happen with current logic but kept for safety.
            print(f"{case!r}: Error - {e}")

    # Additional explicit test to ensure int and float work correctly alongside edge cases.
    assert PositivityChecker.is_positive(10) is True, "Positive integer failed."
    assert PositivityChecker.is_positive(-10) is False, "Negative integer passed as positive."
    assert PositivityChecker.is_positive(0.0) is False, "Zero passed as positive."
    print("All assertions passed.")