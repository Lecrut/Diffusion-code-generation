class ComparisonTool:
    """A utility class to compare two values efficiently."""

    def check_greater(self, value1, value2):
        """
        Compares two values and returns True if value1 is strictly greater than value2, False otherwise.
        
        Args:
            value1 (any comparable type): The first value to compare.
            value2 (any comparable type): The second value to compare.
            
        Returns:
            bool: True if value1 > value2, else False.
        """
        return value1 > value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    tool = ComparisonTool()

    test_cases = [
        (5, 3),           # Expected: True
        (10, 10),         # Expected: False (equal)
        (-2, -4),         # Expected: True (-2 is greater than -4)
        ("apple", "banana"), # Expected: False ('a' < 'b')
        ([3], [1, 2]),    # Expected: True ([3] > [1, 2]) based on list comparison rules
        (True, False),    # Expected: True
    ]

    for val1, val2 in test_cases:
        result = tool.check_greater(val1, val2)
        print(f"{val1} > {val2}: {result}")