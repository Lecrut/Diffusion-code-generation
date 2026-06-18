class ValueChecker:
    """A professional class designed to check inequality between two values."""
    
    def __init__(self):
        pass
    
    def are_different(self, val1, val2):
        """
        Efficiently checks if the provided values are not equal.
        
        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.
            
        Returns:
            bool: True if val1 is not equal to val2, False otherwise.
        """
        return val1 != val2

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    checker = ValueChecker()

    # Test 1: Integers are different
    result_ints = checker.are_different(5, 10)
    
    # Test 2: Floats with same value (different representation possible but equal in logic here simplified to standard comparison)
    result_floats_same = checker.are_different(3.14, 3.14)
    
    # Test 3: Strings are different
    result_strings = checker.are_different("hello", "world")
    
    # Test 4: None and integer
    result_none_int = checker.are_different(None, 0)

    print(f"Integers (5 vs 10): {result_ints}")      # Expected True
    print(f"Floats same value (3.14 vs 3.14): {result_floats_same}")   # Expected False
    print(f"Strings ('hello' vs 'world'): {result_strings}")             # Expected True
    print(f"None and integer: {result_none_int}")                         # Expected True