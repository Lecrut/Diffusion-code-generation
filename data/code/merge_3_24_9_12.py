"""Utility module to check negativity of numeric values."""

class NumberUtils:
    """A utility class providing methods for basic number operations."""

    @staticmethod
    def is_negative(value):
        """
        Check if a given value is negative.

        Args:
            value (int | float | None): The numerical value to check.

        Returns:
            bool: True if the value is strictly less than zero, False otherwise.
        
        Raises:
            TypeError: If the input is not an instance of int or float.
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected int or float, got {type(value).__name__}")

        return value < 0

if __name__ == '__main__':
    # Sample values to test the is_negative static method without user input.
    sample_values = [10, -5, 0.0, -3.4, None]

    for val in sample_values:
        try:
            result = NumberUtils.is_negative(val)
            print(f"Is {val!r} negative? {result}")
        except TypeError as te:
            # Handling cases where the input type is not supported (e.g., None).
            print(f"Error checking {val}: {te}")

    # Testing with explicit non-numeric types to verify error handling.
    test_cases = ["negative string", 10]
    for case in test_cases:
        if isinstance(case, str):
            try:
                NumberUtils.is_negative(case)
            except TypeError as te:
                print(f"Caught expected type error for '{case}': {te}")
        elif isinstance(case, int | float):
            result = NumberUtils.is_negative(case)
            status = "Negative" if result else "Non-negative or zero"
            print(f"{case!r}: {status}")