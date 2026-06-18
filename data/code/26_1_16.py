class ComparisonUtils:
    @staticmethod
    def check_greater(val1, val2):
        """
        Checks if val1 is strictly greater than val2 using direct comparison operators.
        
        Args:
            val1 (any comparable type): The first value to compare.
            val2 (any comparable type): The second value to compare.
            
        Returns:
            bool: True if val1 > val2, False otherwise.
        """
        return val1 > val2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (50, 30),      # Expected: True
        (10, 10),      # Expected: False (equal)
        (-5, -20),     # Expected: True
        ("apple", "banana"),  # Expected: False ('a' < 'b')
        ("zebra", "ant"),   # Expected: True ('z' > 'a')
    ]

    utils = ComparisonUtils()

    for i, (val1, val2) in enumerate(test_cases):
        result = utils.check_greater(val1, val2)
        print(f"Test case {i + 1}: check_greater({repr(val1)}, {repr(val2)}) -> {result}")