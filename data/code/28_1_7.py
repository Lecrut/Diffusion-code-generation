class ComparisonUtils:
    """A utility class providing comparison operations."""

    @staticmethod
    def check_if_greater(a, b):
        """
        Compares two arguments to determine if 'a' is strictly greater than 'b'.

        This method handles integers and floating-point numbers. If types are 
        incompatible for numeric comparison (e.g., string vs number), it raises a TypeError.

        Args:
            a: The first value to compare.
            b: The second value to compare.

        Returns:
            bool: True if 'a' > 'b', False otherwise.

        Raises:
            TypeError: If the types of 'a' and 'b' are not numeric (int or float).
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a > b
        else:
            raise TypeError("Both arguments must be integers or floats.")

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without user input
    
    # Test 1: Integers where first is greater
    result_1 = ComparisonUtils.check_if_greater(5, 3)
    print(f"Is 5 > 3? {result_1}")

    # Test 2: Floats where second is greater (expect False)
    result_2 = ComparisonUtils.check_if_greater(4.5, 6.0)
    print(f"Is 4.5 > 6.0? {result_2}")

    # Test 3: Equal values (expect False since it's strictly greater)
    try:
        result_3 = ComparisonUtils.check_if_greater(10, 10)
        print(f"Is 10 > 10? {result_3}")
    except TypeError as e:
        # This block won't be executed for equal ints/floats based on logic above unless we wanted strict type check failure. 
        # Based on the requirement, standard comparison works fine for equals returning False.
        print(f"Error occurred unexpectedly: {e}")

    # Test 4: Invalid types (expect TypeError)
    try:
        result_4 = ComparisonUtils.check_if_greater("5", 3)
        print(f"Is '5' > 3? {result_4} - This path should ideally not be reached given the logic")
    except TypeError as e:
        print(f"Expected error for incompatible types caught correctly.")

    # Test 5: Negative numbers
    result_5 = ComparisonUtils.check_if_greater(-2, -10)
    print(f"Is -2 > -10? {result_5}")