import sys

class ComparisonTool:
    """A utility class to compare two values efficiently."""

    def check_greater(self, value1, value2):
        """
        Determines if value1 is strictly greater than value2.
        
        Handles potential type errors gracefully by catching exceptions 
        and returning False in case of comparison failure or unsupported types.
        
        Args:
            value1 (any): The first value to compare.
            value2 (any): The second value to compare.
            
        Returns:
            bool: True if value1 > value2, otherwise False.
        """
        try:
            return value1 > value2
        except TypeError:
            # Gracefully handle cases where types cannot be compared directly
            return False

if __name__ == '__main__':
    tool = ComparisonTool()

    # Sample test cases with hard-coded values
    samples = [
        (5, 3),           # Should return True
        ("apple", "banana"),  # String comparison works lexicographically -> False ('a' < 'b')
        ([1], [2]),       # List comparison works element-wise -> False
        ((1,), (0.9)),    # Tuple vs float -> True
        (True, False),    # Boolean: True > False is True in Python
        ("", " "),        # Empty string vs space -> False ('' < ' ')
        ([], [1]),        # List comparison -> True
    ]

    print("Running ComparisonTool check_greater tests...\n")

    for i, (v1, v2) in enumerate(samples):
        result = tool.check_greater(v1, v2)
        status = "PASS" if result == (v1 > v2) else "FAIL"
        # Note: For the purpose of this task, we assume standard Python comparison rules apply.
        # We print the raw boolean from operator to verify correctness against built-in logic where possible.
        
        try:
            expected = v1 > v2
        except TypeError:
            expected = False  # If built-ins fail too, our tool should also return False

        if result == expected:
            status = "PASS"
            
        print(f"Test {i+1}: check_greater({v1!r}, {v2!r})")
        print(f"Result: {result} | Expected (built-in): {expected}")
        print(f"Status: {'✓' if result == expected else '✗'}\n")

    # Additional test for type error handling explicitly
    try:
        tool.check_greater("string", 123)
        print("Test Type Mismatch: PASS (returned False instead of raising)")
    except TypeError as e:
        print(f"Test Type Mismatch: FAIL (raised {e})")

    # Test with None and other edge cases that might raise errors in some contexts but not others
    test_cases_edge = [
        ("a", "b"),       # Strings -> False
        ([1, 2], [3]),    # Lists -> True
        ((True,), (False,)), # Tuples of booleans -> True
    ]

    print("\nEdge Case Tests:")
    for v1, v2 in test_cases_edge:
        res = tool.check_greater(v1, v2)
        try:
            exp = v1 > v2
        except TypeError:
            exp = False
        
        status = "PASS" if res == exp else "FAIL"
        print(f"{status}: check_greater({v1!r}, {v2!r}) -> {res} (expected {exp})")

    # Final confirmation that no external inputs were used
    print("\nAll tests completed without user input or network access.")