class ComparisonTool:
    def check_greater(self, a, b):
        """
        Compares two values using Python's built-in comparison operator ('>').
        
        Args:
            a (any comparable type): The first value to compare.
            b (any comparable type): The second value to compare.
            
        Returns:
            bool: True if 'a' is strictly greater than 'b', False otherwise.
        """
        return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    tool = ComparisonTool()

    test_cases = [
        (10, 5),       # Should be True
        (-3, -6),      # Should be True
        (4.2, 4.2),    # Should be False (equal)
        ("hello", "world"),  # String comparison: 'h' < 'w', so should be False
        ([1, 2], [0]),   # List comparison: lists compare element by element, should be True? No, [1] > [0] is True. Wait: [1]>[0]? Yes because first element 1>0. Correct.
    ]

    for val_a, val_b in test_cases:
        result = tool.check_greater(val_a, val_b)
        print(f"{val_a} vs {val_b}: {'greater' if result else 'not greater'}")