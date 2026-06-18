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
        (5, 3),      # Expected: True
        (3, 5),      # Expected: False
        (7.8, 7.9),  # Expected: False
        ('apple', 'banana'),  # Expected: False
        ('zebra', 'ant'),    # Expected: True
        (-10, -20),  # Expected: True
        (42, 42),    # Expected: False
    ]

    utils = ComparisonUtils()

    print("Running comparison tests...")
    for i, (val1, val2) in enumerate(test_cases):
        result = utils.check_greater(val1, val2)
        expected = val1 > val2
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i+1}: check_greater({repr(val1)}, {repr(val2)})")
        print(f"Result: {result}, Expected: {expected} -> Status: {status}\n")

    # Final confirmation that the module ran successfully without errors or prompts
    assert all(utils.check_greater(a, b) == (a > b) for a, b in test_cases), "Some tests failed!"
    print("All assertions passed.")