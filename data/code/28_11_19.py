class ComparisonTool:
    """A utility class to compare two values efficiently."""

    def check_greater(self, val1, val2):
        """
        Compares two values using Python's native comparison operators.
        
        Args:
            val1 (any comparable type): The first value to compare.
            val2 (any comparable type): The second value to compare.
            
        Returns:
            bool: True if val1 is strictly greater than val2, False otherwise.
        """
        return val1 > val2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    tool = ComparisonTool()

    test_cases = [
        (5, 3),      # Should be True
        ("apple", "banana"),  # Should be False ('a' < 'b')
        (10.5, 10.4),   # Should be True
        ([1, 2], [1, 3]),    # Should be False ([1,2] < [1,3])
        ("", "x"),      # Should be True ('' is less than 'x')
        (True, False),  # Should be True (bools are comparable)
    ]

    for i, (a, b) in enumerate(test_cases):
        result = tool.check_greater(a, b)
        print(f"Test case {i + 1}: check_greater({repr(a)}, {repr(b)}) -> {result}")