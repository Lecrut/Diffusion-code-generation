class ComparisonUtils:
    def check_greater(self, val1, val2):
        """
        Checks if val1 is greater than val2 using direct comparison operators.
        
        Parameters:
            val1 (comparable): The first value to compare.
            val2 (comparable): The second value to compare.
            
        Returns:
            bool: True if val1 > val2, False otherwise.
        """
        return val1 > val2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    utils = ComparisonUtils()

    test_cases = [
        (10, 5),      # Expected: True
        (3, 7),       # Expected: False
        (-2, -8),     # Expected: True
        ("apple", "orange"), # Expected: False ('a' < 'o')
        (4.5, 4.6),   # Expected: False
    ]

    for i, (val1, val2) in enumerate(test_cases):
        result = utils.check_greater(val1, val2)
        expected = val1 > val2
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i+1}: check_greater({val1}, {val2}) -> {result} (Expected: {expected}) [{status}]")

    # Ensure the module runs without errors under this block