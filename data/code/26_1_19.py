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
    # Hard-coded sample values for testing without any user input or external dependencies
    
    test_cases = [
        (50, 30),      # Expected: True
        (10, 10),      # Expected: False (equal)
        (-5, -20),     # Expected: True
        ("apple", "banana"),  # Expected: True ('a' < 'b')
        ([1, 2], [3]),       # Expected: True
    ]

    utils = ComparisonUtils()

    for i, (val1, val2) in enumerate(test_cases):
        result = utils.check_greater(val1, val2)
        expected = val1 > val2
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i+1}: check_greater({val1}, {val2}) -> {result} (Expected: {expected}) [{status}]")