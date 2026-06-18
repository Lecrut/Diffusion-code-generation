class ComparisonTool:
    """A utility class to compare two values efficiently."""

    def check_greater(self, value1, value2):
        """
        Compare two provided values and return True if value1 is greater than value2, False otherwise.
        
        Args:
            value1 (any comparable type): The first value to be compared.
            value2 (any comparable type): The second value to be compared.
            
        Returns:
            bool: True if value1 > value2, False otherwise.
        """
        return value1 > value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    tool = ComparisonTool()

    test_cases = [
        (50, 30),      # Expected: True
        ("apple", "banana"),  # Expected: False ('a' < 'b')
        (-10.5, -20.7),   # Expected: True
        ([], []),         # Expected: False (equal lists)
    ]

    for val1, val2 in test_cases:
        result = tool.check_greater(val1, val2)
        print(f"check_greater({val1!r}, {val2!r}) returned {result}")