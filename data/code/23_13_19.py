"""
Module to compare two strings lexicographically.

This module provides a function that returns a detailed comparison object,
including length difference and index of first differing character.
"""

class StringComparisonResult:
    """A data class representing the result of string comparison."""

    def __init__(self, s1_index=None, len_diff=0):
        self.s1_index = s1_index  # Index in s1 where they differ (None if equal or one is prefix)
        self.len_diff = len_diff  # Length of first string minus length of second

def compare_strings(s1: str, s2: str) -> StringComparisonResult:
    """
    Compare two strings lexicographically.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.

    Returns:
        StringComparisonResult: An object containing the index of the first 
                                differing character and the length difference.
    
    Raises:
        TypeError: If either argument is not a string.
    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Both arguments must be strings.")

    min_len = len(s1) if len(s1) < len(s2) else len(s2)

    for i in range(min_len):
        char_s1 = s1[i]
        char_s2 = s2[i]

        # Check if characters differ or one string ends before the other
        if char_s1 != char_s2:
            return StringComparisonResult(i, len(s1) - len(s2))
    
    # Strings are identical up to the length of the shorter string.
    # If lengths were different earlier in this loop? No, we exited because they matched fully.
    # Now check if one is a prefix/substring of another (handled by min_len logic above).
    # Actually, if s1 = "abc", s2 = "abcd". Loop runs 3 times. 
    # i=0: 'a'=='a', continue...
    # If loop finishes without returning, it means all characters up to min_len are equal.
    
    return StringComparisonResult(None, len(s1) - len(s2))

if __name__ == '__main__':
    # Hard-coded sample values for testing purposes. No user input or external files used.
    
    test_cases = [
        ("apple", "banana"),      # Case 1: Different lengths and characters at start
        ("hello", "hello"),       # Case 2: Identical strings
        ("test", "testing"),      # Case 3: One is a prefix of the other (reversed) -> 't'=='t', etc. 
                                  # Actually s1="test" len=4, s2="testing" len=7. min_len=4. All match. Return None index.
        ("python", "py"),         # Case 4: One is a prefix of the other (s1 longer) -> 'p'=='p', etc. 
                                  # Loop runs for length of 'py'. Returns s1_index=None, diff = -2? Wait logic check below.
    ]

    print("Running String Comparison Tests...\n")

    for i, (str_a, str_b) in enumerate(test_cases):
        result = compare_strings(str_a, str_b)
        
        # Format output clearly without markdown fences outside the code block structure if any, 
        # but strictly following "Return only a single complete runnable Python module" means no extra prose.
        print(f"Comparing '{str_a}' vs '{str_b}':")
        print(f"  Length Difference: {result.len_diff}")
        
        if result.s1_index is not None:
            char_at_idx = str_a[result.s1_index]
            # Verify with s2 just to be safe, though guaranteed by loop logic
            expected_char_s2 = str_b[result.s1_index]
            print(f"  First Difference at Index {result.s1_index}: '{char_at_idx}' != '{expected_char_s2}'")
        else:
            if result.len_diff == 0:
                print("  Result: Strings are identical.")
            elif len(str_a) < len(str_b):
                # s1 is a prefix of s2 (e.g., "py" vs "python", but wait my logic above returns None index for py/python? 
                # Let's re-verify the loop.
                # str_a="test", str_b="testing". min_len=4. i=0..3 match. Returns None, diff=-2 (if s1 shorter). Correct.
                # str_a="python", str_b="py". min_len=2. i=0..1 match ('p'=='p', 'y'=='y'). Loop ends. 
                # Returns None index? Yes because loop finished without mismatch found up to length of shorter string.
                print("  Result: First string is a prefix of the second.")
            else:
                print("  Result: Second string is a prefix of the first.")

        print()