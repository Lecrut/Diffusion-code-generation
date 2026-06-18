"""Utility module containing a static method to determine if a number is positive."""

class NumberUtilities:
    """A utility class providing methods for basic numerical operations."""

    @staticmethod
    def is_positive(value):
        """Check if the given value is strictly greater than zero.

        Args:
            value (int | float): The numeric value to check.

        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing the is_positive method.
    test_values = [10, -5, 0.0, 3.14, None]

    print("Testing NumberUtilities.is_positive():")
    for val in test_values:
        if isinstance(val, (int, float)) and not isinstance(val, bool):
            result = NumberUtilities.is_positive(val)
            status = "Positive" if result else "Non-positive"
            print(f"{val} is {status}")
        elif val is None:
            # Handle non-numeric input gracefully in the demo context.
            try:
                float_val = float(val)
                result = NumberUtilities.is_positive(float_val)
                status = "Positive" if result else "Non-positive"
                print(f"{val} ({float_val}) is {status}")
            except (TypeError, ValueError):
                print(f"{val} cannot be evaluated as a number.")
        else:
            print(f"{val} is not a numeric type.")