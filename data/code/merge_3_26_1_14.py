class ComparisonUtils:
    @staticmethod
    def check_greater(val1, val2):
        """Checks if val1 is strictly greater than val2 using direct comparison."""
        return val1 > val2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    test_cases = [
        (5, 3),      # Should be True
        (10, 10),    # Should be False
        (-1, -2),    # Should be True
        ("apple", "banana"),  # String comparison: 'a' < 'b', so False
        (True, False)   # Boolean comparison: True > False is True in Python
    ]

    utils = ComparisonUtils()

    for i, (val1, val2) in enumerate(test_cases):
        result = utils.check_greater(val1, val2)
        print(f"Test case {i + 1}: check_greater({repr(val1)}, {repr(val2)}) is {result}")