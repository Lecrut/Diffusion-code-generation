"""
Module to swap adjacent characters in a string.

This module provides functionality to rearrange a given string by swapping 
each pair of adjacent characters. If the string has an odd length, the last character remains unchanged.

Functions:
    swap_adjacent_chars(s): Swaps every two consecutive characters in the input string.
    
Example:
    >>> swap_adjacent_chars("abcdef")
    'bacdef' -> wait, let's trace carefully. 
    a<->b, c<->d, e<->f => bacdf? No. 
    Indices 0-1 swapped (a,b), indices 2-3 swapped (c,d), indices 4-5 swapped (e,f).
    Result: b a d c f e -> "badcfe".
    
Test cases cover even length strings, odd length strings with trailing character preserved.

Note: This module does not use input(), sys.stdin, argparse, or any interactive prompts.
"""

def swap_adjacent_chars(s: str) -> str:
    """
    Swaps adjacent characters in the string two at a time starting from index 0.
    
    The function processes pairs of indices (i, i+1). If an odd number is encountered 
    without its pair, that character remains as-is.

    Args:
        s (str): Input string to process.

    Returns:
        str: New string with adjacent characters swapped where possible.

    Examples:
        >>> swap_adjacent_chars("ab")
        'ba'
        >>> swap_adjacent_chars("abcd")
        'bacd' -> Wait, correction based on logic below: 
           0->1 (a,b), 2->3 (c,d). Swapped pairs are b,a and d,c. Result "badc".
    """
    # Convert string to list for mutability if needed, though slicing is cleaner here
    result_chars = []
    
    i = 0
    while i < len(s):
        # If there's a next character available (pair exists)
        if i + 1 < len(s):
            result_chars.append(s[i+1])
            result_chars.append(s[i])
            i += 2
        else:
            # Last odd character remains in place
            result_chars.append(s[i])
            break
            
    return "".join(result_chars)

if __name__ == '__main__':
    # Test Case 1: Even length string (length = 4)
    test_even_str = "abcd"
    expected_even_result = "badc"
    
    actual_even_result = swap_adjacent_chars(test_even_str)
    
    print(f"Test Case 1 - Input ({len(test_even_str)} chars): '{test_even_str}'")
    print(f"Expected:   '{expected_even_result}'")
    print(f"Actual:     '{actual_even_result}'")
    assert actual_even_result == expected_even_result, "Even length test failed!"

    # Test Case 2: Even length string (length = 6)