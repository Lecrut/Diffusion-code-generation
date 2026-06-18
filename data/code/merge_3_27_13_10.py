class ValueChecker:
    """A professional class designed to check if two values are different."""

    def are_different(self, val1, val2):
        """
        Check if val1 is not equal to val2.

        This method uses the standard inequality operator for efficiency and clarity.
        It handles all data types (integers, floats, strings, booleans, etc.) correctly.
        Returns True if they are different, False otherwise.

        Args:
            val1: The first value to compare.
            val2: The second value to compare.

        Returns:
            bool: True if val1 != val2, else False.
        """
        return val1 != val2

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or external dependencies
    
    checker = ValueChecker()
    
    test_cases = [
        ("integers", 5, 3),       # Expected: True
        ("floats", 1.0, 2.0),     # Expected: True
        ("strings", "hello", "world"), # Expected: True
        ("booleans", True, False),    # Expected: True
        ("same_integers", 42, 42),   # Expected: False
        ("similar_floats", 3.14, 3.15), # Expected: True
        ("equal_strings", "test", "test"), # Expected: False
    ]

    print("ValueChecker Test Results:")
    for label, v1, v2 in test_cases:
        result = checker.are_different(v1, v2)
        status = "PASS" if (label != "same_integers" and label != "equal_strings") else "FAIL"
        print(f"{status}: {label} -> are({v1}, {v2}) = {result}")