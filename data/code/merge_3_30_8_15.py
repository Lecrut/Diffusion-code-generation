def swap_adjacent_chars(s: str) -> str:
    """
    Swaps adjacent characters in a string two at a time, starting from index 0.
    
    If the string has an odd length, the last character remains unchanged 
    as there is no pair for it to be swapped with.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped where possible.
             Original string is not modified.
             
    Examples:
        >>> swap_adjacent_chars("abcd")
        'badc'
        >>> swap_adjacent_chars("abcde")
        'bacd e'  # Note: spaces added for clarity in this example, actual logic handles odd length by leaving last char alone
        >>> swap_adjacent_chars("")
        ''
    """
    if not s:
        return ""
    
    result = []
    i = 0
    
    while i < len(s):
        # Check if there is a next character to pair with the current one
        if i + 1 < len(s):
            # Swap characters at index i and i+1, then move two steps forward
            result.append(s[i + 1])
            result.append(s[i])
            i += 2
        else:
            # Odd length case: append the last character as is (no swap possible)
            result.append(s[i])
            break
            
    return "".join(result)

if __name__ == '__main__':
    # Test Case 1: Even length string with clear swaps
    test_even = "abcdef"
    expected_even = "bacdef"
    
    # Test Case 2: Odd length string where the last character remains unchanged
    test_odd = "abcde"
    expected_odd = "badce"
    
    # Test Case 3: Empty string edge case
    test_empty = ""
    expected_empty = ""

    print("Test Case 1 (Even Length):")
    result_even = swap_adjacent_chars(test_even)
    assert result_even == expected_even, f"Failed for even length. Expected '{expected_even}', got '{result_even}'"
    print(f"Input: {test_even}")
    print(f"Output: {result_even} (PASS)")

    print("\nTest Case 2 (Odd Length):")
    result_odd = swap_adjacent_chars(test_odd)
    assert result_odd == expected_odd, f"Failed for odd length. Expected '{expected_odd}', got '{result_odd}'"
    print(f"Input: {test_odd}")
    print(f"Output: {result_odd} (PASS)")

    print("\nTest Case 3 (Empty String):")
    result_empty = swap_adjacent_chars(test_empty)
    assert result_empty == expected_empty, f"Failed for empty string. Expected '{expected_empty}', got '{result_empty}'"
    print(f"Input: {test_empty}")
    print(f"Output: {result_empty} (PASS)")

    print("\nAll tests passed successfully.")