class ValueChecker:
    def __init__(self):
        """Initialize the ValueChecker instance."""
        pass
    
    def are_different(self, val1, val2):
        """
        Check if two provided values are not equal.
        
        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.
            
        Returns:
            bool: True if the values are different, False otherwise.
        """
        return val1 != val2

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    checker = ValueChecker()
    
    # Test case 1: Integers
    result_ints = checker.are_different(5, 10)
    print(f"Integers (5 vs 10): {result_ints}")  # Expected: True
    
    # Test case 2: Strings
    result_strings = checker.are_different("hello", "world")
    print(f"Strings ('hello' vs 'world'): {result_strings}")  # Expected: True
    
    # Test case 3: Floats with different precision (should be treated as different)
    result_floats = checker.are_different(1.0, 2.5)
    print(f"Floats (1.0 vs 2.5): {result_floats}")  # Expected: True
    
    # Test case 4: Equal values
    result_equal = checker.are_different(3, 3)
    print(f"Equal Integers (3 vs 3): {result_equal}")  # Expected: False

    # Test case 5: None and Integer
    result_none_int = checker.are_different(None, 0)
    print(f"None vs Integer (None vs 0): {result_none_int}")  # Expected: True
    
    # Test case 6: Complex objects with same value but different identity (handled by != operator correctly for most cases unless custom __eq__ is defined)
    class CustomObj:
        def __init__(self, val):
            self.val = val
        
        def __repr__(self):
            return f"CustomObj({self.val})"

    obj1 = CustomObj(42)
    obj2 = CustomObj(43)
    
    result_custom_diff = checker.are_different(obj1, obj2)
    print(f"Different Objects: {result_custom_diff}")  # Expected: True
    
    obj_same_val = CustomObj(42)
    obj_another_same_val = CustomObj(42)
    
    result_custom_same = checker.are_different(obj_same_val, obj_another_same_val)
    print(f"Same Value Objects (different instances): {result_custom_same}")  # Expected: True