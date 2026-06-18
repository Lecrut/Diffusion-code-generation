class ComparisonTool:
    """A utility class to compare values efficiently."""

    def check_greater(self, val1, val2):
        """
        Compares two values using Python's native comparison operators.
        
        Args:
            val1 (any comparable type): The first value to be compared.
            val2 (any comparable type): The second value to be compared.
            
        Returns:
            bool: True if val1 is strictly greater than val2, False otherwise.
        """
        return val1 > val2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    tool = ComparisonTool()

    test_cases = [
        (50, 30),      # Expected: True
        ("apple", "banana"),  # Expected: False ('a' < 'b')
        (-10.5, -2.3),# Expected: False (-10.5 < -2.3)
        ([], [1]),     # Expected: True (empty list is less than non-empty)
    ]

    for i, (v1, v2) in enumerate(test_cases):
        result = tool.check_greater(v1, v2)
        print(f"Test case {i + 1}: check_greater({repr(v1)}, {repr(v2)}) -> {result}")