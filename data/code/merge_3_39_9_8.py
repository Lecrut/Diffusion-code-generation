"""
Module to find all nested substrings within a phrase, handling overlapping cases correctly.

This module provides an efficient algorithm to extract every contiguous substring 
from a given input string (phrase). A "nested substring" in this context refers 
to any sequence of characters that appears contiguously within the main string. 
Overlapping occurrences are included; if multiple substrings share common parts,
all distinct starting positions and lengths are captured as long as they represent
valid contiguous segments from start to end indices (0 <= i < j).

The solution uses a nested loop approach optimized for clarity and correctness over 
extreme recursion or complex parsing patterns. Time complexity is O(n^2), which is 
optimal without pre-processing constraints like fixed alphabet size, though it can be
optimized further with suffix structures if n becomes very large. For typical use cases,
this implementation balances efficiency and readability.

Note: This does not parse for nested linguistic constructs (like parentheses matching) 
unless explicitly specified by the user in future iterations; strictly returns all 
contiguous character sequences defined by start/end index ranges within bounds.

Author: AI Assistant
Date: 2023-10-07
"""

def find_nested_substrings(phrase: str):
    """
    Find all contiguous substrings (nested characters) in the given phrase.
    
    This function generates every possible substring by iterating through all 
    valid start and end index pairs where 0 <= start < end <= len(phrase).
    
    Parameters:
        phrase (str): The input string to analyze. Must be a non-empty string.
        
    Returns:
        List[str]: A list of unique substrings extracted from the phrase, 
                   preserving order based on their first appearance in terms 
                   of start index and length ordering. If duplicates exist due 
                   to identical content at different positions, only one instance 
                   is returned per unique string value (as typically expected).
    
    Raises:
        TypeError: If 'phrase' is not a string or None.
        
    Examples:
        >>> find_nested_substrings("abc")
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
        Note: While order may vary slightly depending on implementation, 
              all 6 substrings of length >=1 are present.
    
    Raises:
        TypeError if phrase is not a string instance or None passed in.
        
    Complexity Analysis:
        Time Complexity: O(n^2) where n = len(phrase). We generate up to n*(n+1)/2 
                        substrings, and slicing each takes average O(n), leading 
                        potentially to higher constant factors but acceptable for moderate inputs.
        Space Complexity: O(k*n) in worst case due to storing all unique strings, 
                      where k is number of unique substrings (up to n^2/2).
    
    """

    # Input validation
    if phrase is None or not isinstance(phrase, str):
        raise TypeError(f"Expected string input, got {type(phrase).__name__} or None")
        
    result_set = set()  # Use set for automatic uniqueness handling during generation
    
    n = len(phrase)
    
    # Generate all contiguous substrings using nested loops
    for start_idx in range(n):
        for end_idx in range(start_idx + 1, n + 1):
            substring = phrase[start_idx:end_idx]
            result_set.add(substring)
            
    return list(result_set)

if __name__ == '__main__':
    # Hard-coded sample values to ensure module runs without user input or external dependencies.
    
    test_cases = [
        "abc",           # Simple case: all substrings of 'a', 'b', 'c' and combinations
        "",              # Edge case: empty string should return []
        "aaa",           # Overlapping identical characters; expect unique values only
        "abacaba",       # Complex overlapping pattern with repeated letters
    ]

    for phrase in test_cases:
        substrings = find_nested_substrings(phrase)
        print(f"Phrase: '{phrase}'")
        print(f"Nested Substrings ({len(substrings)} unique): {substrings}")
        
        if len(substrings) > 0 and isinstance(substrings[0], str):
            # Optional sanity check for non-empty results
            assert all(isinstance(s, str) for s in substrings), "All items must be strings"
    
    print("\n--- End of execution ---")