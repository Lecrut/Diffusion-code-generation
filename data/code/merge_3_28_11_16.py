class ComparisonTool:
    def check_greater(self, value1, value2):
        """
        Compares two values using a single efficient comparison operator.
        
        Args:
            value1 (any comparable type): The first value to compare.
            value2 (any comparable type): The second value to compare.
            
        Returns:
            bool: True if value1 is strictly greater than value2, False otherwise.
        """
        return value1 > value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies
    
    tool = ComparisonTool()
    
    # Test cases with various data types to ensure efficient comparison works correctly
    test_cases = [
        (10, 5),           # integers: True expected
        ("apple", "banana"), # strings: False expected ('a' < 'b')
        (3.14, 2.71),     # floats: True expected
        ([1, 2], [1, 3]),   # lists (element-wise not supported but operator handles it): depends on implementation details, generally handled by Python's comparison logic efficiently
        ("", "a"),         # empty string vs char: False expected
    ]

    for val1, val2 in test_cases:
        result = tool.check_greater(val1, val2)
        print(f"check_greater({val1!r}, {val2!r}) = {result}")