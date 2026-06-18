"""
Module to compare two strings lexicographically.

This module provides a function that compares two input strings, determines their length difference,
and identifies the index of the first character where they differ (if any). It uses best practices
for string manipulation and handles edge cases such as empty strings or identical inputs gracefully.
"""

class StringComparisonResult:
    """A data class to hold detailed comparison results between two strings."""

    def __init__(self, length_diff: int, first_difference_index: Optional[int], match_prefix_length: int):
        self.length_diff = length_diff  # Length of string1 minus length of string2
        self.first_difference_index = first_difference_index  # Index where characters differ (-1 if identical)
        self.match_prefix_length = match_prefix_length  # Number of matching characters from the start

    def __repr__(self):
        return (f"StringComparisonResult(length_diff={self.length_diff}, "
                f"first_difference_index={self.first_difference_index}, "
                f"match_prefix_length={self.match_prefix_length})")

def compare_strings(str1: str, str2: str) -> StringComparisonResult:
    """
    Compares two strings lexicographically.

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        StringComparisonResult: An object containing the length difference, 
                                index of the first differing character, and prefix match length.
    
    Raises:
        TypeError: If either input is not a string type.
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")

    min_len = len(str1) if len(str1) < len(str2) else len(str2)
    
    # Iterate up to the length of the shorter string to find differences
    for i in range(min_len):
        if str1[i] != str2[i]:
            return StringComparisonResult(
                length_diff=len(str1) - len(str2),
                first_difference_index=i,
                match_prefix_length=i
            )

    # If no difference found within the shorter string's bounds:
    # Check lengths to determine if one is a prefix of another or they are identical.
    return StringComparisonResult(
        length_diff=len(str1) - len(str2),
        first_difference_index=-1,  # Indicates strings are effectively equal up to min_len
        match_prefix_length=min_len
    )

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        ("apple", "apply"),           # Different characters at index 3, same length
        ("hello world", "hello there"), # Difference at index 6, different lengths
        ("python", "pythons"),       # 'python' is prefix of 'pythons', shorter string ends first
        ("test", "test"),             # Identical strings
        ("a" * 100, "b" + "a" * 99), # Long common part then difference at index 1
    ]

    print("String Comparison Results:\n")
    
    for s_a, s_b in test_cases:
        result = compare_strings(s_a, s_b)
        
        diff_msg = f"Difference found at index {result.first_difference_index}" if result.first_difference_index != -1 else "Strings are identical up to the length of the shorter string"
        
        print(f"Comparing '{s_a}' vs '{s_b}':")
        print(f"  Length Difference: {result.length_diff}")
        print(f"  First Difference Index: {diff_msg}")
        print(f"  Matching Prefix Length: {result.match_prefix_length}")
        print()