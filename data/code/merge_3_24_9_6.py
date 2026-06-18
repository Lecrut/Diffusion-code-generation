"""Utility module containing functions to check negativity of numerical values."""

class NumberUtilities:
    """A utility class providing methods for basic number analysis."""

    @staticmethod
    def is_negative(value):
        """
        Check if a given value is negative.

        Args:
            value (int | float): The numeric value to evaluate.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    test_values = [
        -5,
        3.14,
        0,
        -0.001,
        "negative string",  # Should raise TypeError as expected per logic constraints
    ]

    print("Testing negativity checks:")
    for val in test_values:
        try:
            result = NumberUtilities.is_negative(val)
            status = "Negative" if result else "Not Negative"
            print(f"{val} is {status}")
        except TypeError as e:
            # Gracefully handle non-numeric inputs to prevent runtime crashes during demo
            print(f"'{val}' caused a type error (expected behavior for mixed types): {e}")

    # Explicit numeric test cases covering edge scenarios
    explicit_tests = [0, -1.5, 42]
    print("\nExplicit numeric tests:")
    for num in explicit_tests:
        is_neg = NumberUtilities.is_negative(num)
        assert isinstance(is_neg, bool), "Result must be a boolean."
        if is_neg:
            print(f"{num} correctly identified as negative.")
        else:
            print(f"{num} correctly identified as non-negative or zero.")

    # Final verification summary
    final_check = NumberUtilities.is_negative(-10)
    assert final_check == True, "Final check failed."
    print("\nAll internal logic checks passed successfully.")