"""Utility module containing a static method to determine if a number is positive."""

class NumberUtilities:
    """A utility class providing methods for basic numerical operations."""

    @staticmethod
    def is_positive(value):
        """Check if the given value is strictly greater than zero.

        Args:
            value (int | float): The numeric value to evaluate.

        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing the is_positive method without user input.
    test_values = [10, -5, 0.0, 3.14, None]

    print("Testing NumberUtilities.is_positive():")
    for val in test_values:
        try:
            result = NumberUtilities.is_positive(val) if val is not None else "Error"
            print(f"is_positive({val}) -> {result}")
        except TypeError as e:
            # Handle cases where non-numeric types are passed to avoid runtime errors.
            print(f"is_positive({val}) -> Error (Type error): {e}")

    # Additional explicit test with a valid positive and negative integer for clarity.
    sample_cases = [42, -7]
    print("\nExplicit Sample Cases:")
    for num in sample_cases:
        status = "Positive" if NumberUtilities.is_positive(num) else "Non-positive (zero or negative)"
        print(f"{num} is {status}")