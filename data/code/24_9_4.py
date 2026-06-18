"""Utility module containing a static method to check if a number is negative."""

class NumberUtils:
    """A utility class providing methods for basic numerical checks."""

    @staticmethod
    def is_negative(value):
        """Check if the provided value is strictly less than zero.

        Args:
            value (int | float): The numeric value to evaluate.

        Returns:
            bool: True if value < 0, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing the is_negative method
    test_values = [
        -5,      # Should be negative
        0,       # Not negative (zero)
        3.14,    # Positive float
        -2.718,  # Negative float
        "not a number",  # Will raise TypeError if passed directly; handled below for safety in demo
    ]

    print("Testing NumberUtils.is_negative():")
    for val in test_values:
        try:
            result = NumberUtils.is_negative(val)
            status = "Negative" if result else "Non-negative"
            print(f"{val!r} -> {status}")
        except TypeError as te:
            # Gracefully handle non-numeric input to keep the script runnable without errors
            print(f"{val!r} -> Error (expected for non-numbers): {te}")

    # Explicit test with a known negative integer
    explicit_test = NumberUtils.is_negative(-10)
    assert explicit_test is True, "Explicit negative check failed"
    print("\nAll assertions passed.")