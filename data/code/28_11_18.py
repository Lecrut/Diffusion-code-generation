class ComparisonTool:
    """A utility class to compare two values efficiently."""

    def check_greater(self, value1, value2):
        """
        Compares two values and returns True if value1 is strictly greater than value2, False otherwise.
        
        Args:
            value1 (any comparable type): The first value to be compared.
            value2 (any comparable type): The second value to be compared.
            
        Returns:
            bool: True if value1 > value2, else False.
        """
        return value1 > value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    tool = ComparisonTool()

    test_cases = [
        (50, 49),      # Expected: True
        (3.14, 3.2),   # Expected: False
        ("apple", "banana"),  # Expected: False
        (-10, -5),     # Expected: False
        (True, False), # Expected: True
    ]

    for val_a, val_b in test_cases:
        result = tool.check_greater(val_a, val_b)
        print(f"{val_a} > {val_b}: {result}")