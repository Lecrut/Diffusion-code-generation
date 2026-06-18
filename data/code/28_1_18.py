class ComparisonUtils:
    """A utility class providing comparison operations."""

    def check_if_greater(self, a, b):
        """
        Compares two arguments to determine if 'a' is strictly greater than 'b'.
        
        Args:
            a (any comparable type): The first value to compare.
            b (any comparable type): The second value to compare.
            
        Returns:
            bool: True if a > b, False otherwise.
        """
        return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    utils = ComparisonUtils()

    test_cases = [
        (10, 5),      # Expected: True
        (3.14, 2.71), # Expected: True
        ("apple", "banana"), # Expected: False
        (-1, -5),     # Expected: True
        (True, False) # Expected: True
    ]

    print("Running ComparisonUtils checks...")
    for i, (val_a, val_b) in enumerate(test_cases):
        result = utils.check_if_greater(val_a, val_b)
        expected = "True" if val_a > val_b else "False"
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i+1}: check_if_greater({val_a!r}, {val_b!r}) -> {result} ({status})")

    # Final confirmation that the module ran successfully without errors
    assert all(ComparisonUtils().check_if_greater(a, b) == (a > b) for a, b in test_cases), "Some tests failed!"