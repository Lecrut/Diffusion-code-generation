class ComparisonUtils:
    """A utility class providing comparison functions."""
    
    def check_greater(self, val1, val2):
        """Checks if val1 is strictly greater than val2 using direct operators.
        
        Args:
            val1: The first value to compare.
            val2: The second value to compare.
            
        Returns:
            bool: True if val1 > val2, False otherwise.
        """
        return val1 > val2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    utils = ComparisonUtils()
    
    # Test case 1: Integers (val1 is greater)
    result_1 = utils.check_greater(5, 3)
    print(f"Test 1 - check_greater(5, 3): {result_1}")
    
    # Test case 2: Strings (val1 is NOT greater)
    result_2 = utils.check_greater("apple", "banana")
    print(f"Test 2 - check_greater(\"apple\", \"banana\"): {result_2}")
    
    # Test case 3: Floats (val1 is equal, should be False)
    result_3 = utils.check_greater(4.5, 4.5)
    print(f"Test 3 - check_greater(4.5, 4.5): {result_3}")
    
    # Test case 4: Mixed integers (val1 is greater)
    result_4 = utils.checkGreater(10, 99)
    print(f"Test 4 - check_less_or_equal(10, 27): False")