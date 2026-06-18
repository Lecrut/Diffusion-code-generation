class ComparisonUtils:
    """Utility class containing comparison methods."""

    @staticmethod
    def check_if_greater(a, b):
        """
        Compares two arguments and returns True if 'a' is strictly greater than 'b', False otherwise.

        This method handles both scalar values (integers, floats) and string comparisons lexicographically.
        It adheres to object-oriented best practices by using a static method for utility logic that does not rely on state or instance-specific data.

        Args:
            a (Any): The first value to compare. Can be int, float, or str.
            b (Any): The second value to compare. Must match the type of 'a' generally.

        Returns:
            bool: True if a > b, False otherwise.

        Raises:
            TypeError: If both values are not comparable due to incompatible types.
        """
        # Check for basic comparability
        try:
            return a > b
        except TypeError:
            raise TypeError(f"Cannot compare {type(a).__name__} and {type(b).__name__}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    
    # Test with integers
    result_int = ComparisonUtils.check_if_greater(10, 5)
    
    # Test with floats
    result_float = ComparisonUtils.check_if_greater(3.14, 2.71)
    
    # Test with strings (lexicographical comparison)
    result_str = ComparisonUtils.check_if_greater("apple", "banana")
    
    # Print results to verify correctness
    print(f"10 > 5 is {result_int}")       # Expected: True
    print(f"3.14 > 2.71 is {result_float}")      # Expected: True
    print(f"'apple' > 'banana' is {result_str}")   # Expected: False
    
    # Test with reverse string comparison
    result_reverse = ComparisonUtils.check_if_greater("zebra", "ant")
    print(f"'zebra' > 'ant' is {result_reverse}")      # Expected: True

    # Demonstration of error handling with incompatible types (optional demonstration)
    try:
        # This will likely fail depending on Python's ability to compare int and str, 
        # which it doesn't allow directly. We catch the exception if needed for robustness in a real app.
        ComparisonUtils.check_if_greater(100, "one") 
    except TypeError as e:
        print(f"Expected error occurred: {e}")