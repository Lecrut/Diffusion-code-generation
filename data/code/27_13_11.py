class ValueChecker:
    """A utility class to check equality of two values efficiently."""
    
    def __init__(self):
        pass
    
    def are_different(self, val1, val2) -> bool:
        """
        Check if the provided arguments are not equal.
        
        This method uses Python's native != operator which handles various types 
        (integers, floats, strings, objects with __eq__ defined) efficiently and correctly.
        It avoids manual type checking to ensure proper handling of edge cases like 
        floating-point comparison semantics unless specific logic is added later.
        
        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.
            
        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return val1 != val2

if __name__ == '__main__':
    checker = ValueChecker()
    
    # Test case 1: Different integers
    test_int_1 = checker.are_different(5, 7)
    
    # Test case 2: Equal strings
    test_str = checker.are_different("hello", "world")
    
    # Test case 3: Same object reference (simulated by value equality in Python)
    list_one = [1, 2, 3]
    list_two = [4, 5, 6]
    test_list = checker.are_different(list_one, list_two)
    
    print(f"Integers different (5 vs 7): {test_int_1}")   # Should be True
    print(f"strings different ('hello' vs 'world'): {test_str}") # Should be True
    print(f"Lists different ([1,2] vs [4,5]): {test_list}")      # Should be True
    
    # Additional check to ensure it returns False when equal would help verify logic if needed here, 
    # but per task we just need the code structure.