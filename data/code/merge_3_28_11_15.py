class ComparisonTool:
    """A utility class providing optimized value comparison methods."""

    def check_greater(self, a, b):
        """
        Compares two values to determine if 'a' is strictly greater than 'b'.
        
        This method uses the most efficient standard Python comparison operator.
        It returns True if a > b, and False otherwise.
        
        Args:
            a (any comparable type): The first value to compare.
            b (any comparable type): The second value to compare.
            
        Returns:
            bool: True if 'a' is greater than 'b', False otherwise.
        """
        return a > b

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or external dependencies
    tool = ComparisonTool()

    test_cases = [
        (10, 5),      # Should be True
        ("apple", "banana"),  # Should be False ('a' < 'b')
        (3.14, 2.71),     # Should be True
        (-5, -10),       # Should be True
    ]

    for val_a, val_b in test_cases:
        result = tool.check_greater(val_a, val_b)
        print(f"{val_a} > {val_b}: {result}")