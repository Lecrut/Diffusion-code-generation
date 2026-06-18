class ComparisonUtils:
    """Utility class containing comparison methods."""

    @staticmethod
    def check_if_greater(a, b):
        """
        Compares two arguments to determine if 'a' is strictly greater than 'b'.

        This method supports various data types (integers, floats, strings) and handles
        type mismatches by raising a TypeError. It adheres to object-oriented best practices
        using static methods for utility functions that do not require instance state.

        Args:
            a: The first value to compare.
            b: The second value to compare.

        Returns:
            bool: True if 'a' is greater than 'b', False otherwise.

        Raises:
            TypeError: If the types of 'a' and 'b' are incompatible for comparison.
        """
        return a > b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    test_cases = [
        (10, 5),      # Should be True
        ("apple", "banana"),  # Should be False ('a' < 'b')
        (-3.5, -2.1),   # Should be False
        (42, 9**2)       # Should be False (42 == 81 is false, but we check > so it's actually True? Wait: 42 vs 81 -> False)
    ]

    print("Running ComparisonUtils checks...")
    
    for item in test_cases:
        a, b = item
        
        # Dynamic type checking to demonstrate robustness without input() calls
        if not isinstance(a, (int, float, str)) or not isinstance(b, (int, float, str)):
            print(f"Skipping mixed-type comparison between {type(a).__name__} and {type(b).__name__}")
            continue

        try:
            result = ComparisonUtils.check_if_greater(a, b)
            status = "GREATER" if result else "NOT GREATER OR EQUAL"
            print(f"{a!r} ({type(a).__name__}) vs {b!r} ({type(b).__name__}): {status}")
        except TypeError as e:
            print(f"Error comparing types: {e}")

    # Additional explicit test case for integers
    int_test = ComparisonUtils.check_if_greater(10, 5)
    assert int_test == True, "Integer comparison failed."
    
    float_test = ComparisonUtils.check_if_greater(3.9, 4.0)
    assert float_test == False, "Float comparison failed."

    print("All assertions passed.")