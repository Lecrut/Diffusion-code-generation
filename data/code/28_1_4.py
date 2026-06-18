class ComparisonUtils:
    """A utility class providing comparison methods."""

    @staticmethod
    def check_if_greater(value1, value2):
        """
        Compares two values to determine if the first is greater than the second.

        This method handles both numeric types (int and float) by attempting conversion.
        If conversion fails for either argument, it raises a TypeError.

        Args:
            value1: The first value to compare.
            value2: The second value to compare.

        Returns:
            bool: True if value1 is strictly greater than value2, False otherwise.

        Raises:
            TypeError: If neither argument can be converted to a number.
        """
        try:
            num1 = float(value1)
            num2 = float(value2)
            return num1 > num2
        except (ValueError, AttributeError):
            raise TypeError("Both arguments must be convertible to numbers.")

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    utils = ComparisonUtils()

    # Test with integers
    result_int_1 = utils.check_if_greater(10, 5)
    print(f"Integers (10 > 5): {result_int_1}")  # Expected: True

    result_int_2 = utils.check_if_greater(3, 7)
    print(f"Integers (3 > 7): {result_int_2}")  # Expected: False

    # Test with floats
    result_float_1 = utils.check_if_greater(3.14, 2.85)
    print(f"Floats (3.14 > 2.85): {result_float_1}")  # Expected: True

    result_float_2 = utils.check_if_greater(0.99, 1.01)
    print(f"Floats (0.99 > 1.01): {result_float_2}")  # Expected: False

    # Test with mixed types that convert to float correctly
    result_mixed = utils.check_if_greater("5", "3")
    print(f"Mixed strings ('5' > '3'): {result_mixed}")  # Expected: True (converted to floats)

    # Demonstrate error handling attempt (commented out as per task requirements, 
    # but logic is present in the class method itself).
    # utils.check_if_greater("a", "b") would raise a TypeError.