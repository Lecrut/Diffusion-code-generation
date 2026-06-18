import re

class PositivityChecker:
    """Utility class to determine if a string represents a positive value."""

    @staticmethod
    def is_positive(value) -> bool:
        """
        Check if the input value represents a strictly positive number.

        This method supports integers, floats, and numeric strings that may contain
        optional whitespace or signs other than '+'. It returns False for zero or non-numeric values.

        :param value: The value to check. Can be an int, float, or string representation of a number.
        :return: True if the value is positive (e.g., > 0), False otherwise.
        """
        # Normalize input: convert strings to numeric types first for consistency in handling
        normalized_value = value

        try:
            num_val = float(normalized_value)
        except (ValueError, TypeError):
            return False

        # Strictly positive means greater than zero, not equal to or less than zero.
        return num_val > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing the utility class without external input.
    test_cases = [123, -456, " +789 ", 0.001, "-0", None, "", True]

    print("Testing PositivityChecker.is_positive() logic:")
    for case in test_cases:
        result = PositivityChecker.is_positive(case)
        # Print type information to demonstrate it works with various inputs if needed,
        # but focuses on the boolean outcome as per task requirements.
        output_str = f"Input: {case!r} -> Positive: {result}"
        print(output_str)