class ComparisonTool:
    """A utility class to compare two values efficiently."""

    def check_greater(self, value1, value2):
        """
        Compares two values using efficient operators and returns True if value1 > value2, False otherwise.

        Args:
            value1 (any comparable type): The first value to be compared.
            value2 (any comparable type): The second value to be compared.

        Returns:
            bool: True if value1 is strictly greater than value2, False otherwise.
        """
        return value1 > value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    tool = ComparisonTool()

    test_cases = [
        (5, 3),       # Expected: True
        (3, 5),       # Expected: False
        (10.5, 9.2),  # Expected: True
        ('apple', 'banana'),  # Expected: False
        ('zebra', 'ant'),    # Expected: True
        (42, 42),     # Expected: False
    ]

    for val1, val2 in test_cases:
        result = tool.check_greater(val1, val2)
        print(f"{val1} > {val2}: {result}")