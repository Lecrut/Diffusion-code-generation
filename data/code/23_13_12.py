"""
Module to compare two strings lexicographically with detailed difference reporting.
This module provides a function that returns an object containing:
- The length of each string.
- The index of the first differing character (or -1 if one is a prefix of another).
- A boolean indicating whether they are equal or identical up to the shorter length.

No external libraries, input prompts, or command-line arguments are used.
"""

class StringComparisonResult:
    """Data class representing the result of comparing two strings."""
    
    def __init__(self, str1_len: int, str2_len: int, first_diff_index: int):
        self.str1_length = str1_len
        self.str2_length = str2_len
        self.first_difference_index = first_diff_index

    def is_equal(self) -> bool:
        """Check if the strings are identical."""
        return (self.str1_length == self.str2_length and 
                self.first_difference_index < 0 or 
                (self.first_difference_index >= 0 and 
                 not any(str1[i] != str2[i] for i in range(self.first_difference_index))))

    def __repr__(self):
        return f"StringComparisonResult(len1={self.str1_length}, len2={self.str2_length}, first_diff_idx={self.first_difference_index})"

def compare_strings_lexicographically(str1: str, str2: str) -> StringComparisonResult:
    """
    Compares two strings lexicographically.

    Returns a detailed comparison object showing the difference in length 
    and the index of the first differing character.

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        StringComparisonResult: An instance containing lengths and the first mismatch index.
    
    Raises:
        TypeError: If inputs are not strings.
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both arguments must be instances of str.")

    len1 = len(str1)
    len2 = len(str2)
    
    # Determine the minimum length to iterate up to
    min_len = min(len1, len2)
    
    first_diff_index = -1
    
    for i in range(min_len):
        if str1[i] != str2[i]:
            first_diff_index = i
            break
            
    return StringComparisonResult(str1_length=len1, str2_length=len2, 
                                   first_difference_index=first_diff_index)

if __name__ == '__main__':
    pass
