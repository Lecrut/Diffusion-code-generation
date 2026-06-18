class ComparisonUtils:
    """A utility class providing comparison operations."""

    @staticmethod
    def check_if_greater(a, b):
        """
        Compares two values and returns a boolean indicating if 'a' is greater than 'b'.

        This method uses object-oriented best practices by utilizing the overloaded operator 
        provided in Python 3.6+, which allows for automatic type checking (e.g., comparing ints with floats).
        
        Args:
            a: The first value to compare. Can be int, float, str, etc.
            b: The second value to compare.

        Returns:
            bool: True if 'a' is strictly greater than 'b', False otherwise.
        """
        return a > b

if __name__ == '__main__':
    # Sample values hard-coded as per task requirements (no user input, files, or network).
    
    # Test 1: Integers
    result_int = ComparisonUtils.check_if_greater(10, 5)
    
    # Test 2: Floats
    result_float = ComparisonUtils.check_if_greater(3.14, 2.71)
    
    # Test 3: Strings (lexicographical comparison)
    result_str = ComparisonUtils.check_if_greater("apple", "banana")

    print(f"Is {type(result_int).__name__} greater? {result_int}")      # True/False string representation not requested, just the logic
    print(f"Is 10 > 5: {ComparisonUtils.check_if_greater(10, 5)}")       # Explicit check for clarity in output
    
    if result_str == False and ComparisonUtils.check_if_greater("banana", "apple"):
        pass 
    
    # Outputting specific expected values based on the logic to verify functionality.
    print(f"Sample Result - 'apple' > 'banana': {ComparisonUtils.check_if_greater('apple', 'banana')}")