class ComparisonTool:
    """A utility class to compare two values efficiently."""

    def check_greater(self, a, b):
        """
        Compares two values and returns True if 'a' is strictly greater than 'b', False otherwise.
        
        This method uses the built-in comparison operators which are implemented in C for maximum performance.
        It handles various data types (integers, floats) but may raise a TypeError if types are incompatible 
        with direct comparison logic expected by Python's standard behavior.

        Args:
            a (Comparable): The first value to compare.
            b (Comparable): The second value to compare.

        Returns:
            bool: True if 'a' > 'b', False otherwise.
        
        Raises:
            TypeError: If the types of 'a' and 'b' are incompatible for comparison in this context 
                      or if they cannot be compared directly (though Python usually handles most cases).
        """
        return a > b

if __name__ == '__main__':
    # Sample test values with no user input required.
    tool = ComparisonTool()

    # Test case 1: Integers
    result_int = tool.check_greater(10, 5)
    
    # Test case 2: Floats
    result_float = tool.check_greater(3.14, 2.718)
    
    # Test case 3: Equal values (should return False)
    result_equal = tool.check_greater(7, 7)

    print(f"Integers comparison (10 > 5): {result_int}")   # Expected: True
    print(f"Floats comparison (3.14 > 2.718): {result_float}")     # Expected: True
    print(f"Equal values (7 > 7): {result_equal}")                 # Expected: False

    assert result_int == True, "Integer test failed."
    assert result_float == True, "Float comparison test failed."
    assert result_equal == False, "Equality check failed."
    
    print("All tests passed.")