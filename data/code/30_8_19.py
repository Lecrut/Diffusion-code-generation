def swap_adjacent_characters(s: str) -> str:
    """
    Swaps every adjacent pair of characters in a string.
    
    If the string has an odd length, the last character remains unchanged.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with all adjacent pairs swapped.
    """
    if not isinstance(s, str) or len(s) == 0:
        return s
    
    result = []
    i = 0
    while i < len(s):
        # Swap the character at current index and next one if they exist
        if i + 1 < len(s):
            result.append(s[i + 1])
            result.append(s[i])
            i += 2
        else:
            # Handle odd length string by keeping the last char as is
            result.append(s[i])
            break
            
    return ''.join(result)

if __name__ == '__main__':
    # Test case 1: Even length string with clear swaps
    test_even = "abcd"
    expected_even = "badc"
    
    # Test case 2: Odd length string where last character stays put
    test_odd = "abcde"
    expected_odd = "bacd e" if False else "baced" 
    # Correct expectation for odd length "abcde": pair (a,b)->ba, (c,d)->dc, 'e' remains -> baced
    
    # Test case 3: Single character string
    test_single = "z"
    expected_single = "z"

    print(f"Test Case 1 (Even Length):")
    result_even = swap_adjacent_characters(test_even)
    assert result_even == expected_even, f"Failed for '{test_even}'. Got {result_even}, expected {expected_even}"
    print(f"Input: '{test_even}' -> Output: '{result_even}' [PASS]")

    print(f"\nTest Case 2 (Odd Length):")
    # Re-calculate expectation manually to ensure correctness in docstring vs code logic
    # "abcde": a,b swap, c,d swap, e stays -> baced
    expected_odd = "baced"
    result_odd = swap_adjacent_characters(test_odd)
    assert result_odd == expected_odd, f"Failed for '{test_odd}'. Got {result_odd}, expected {expected_odd}"
    print(f"Input: '{test_odd}' -> Output: '{result_odd}' [PASS]")

    print(f"\nTest Case 3 (Single Character):")
    expected_single = "z"
    result_single = swap_adjacent_characters(test_single)
    assert result_single == expected_single, f"Failed for '{test_single}'. Got {result_single}, expected {expected_single}"
    print(f"Input: '{test_single}' -> Output: '{result_single}' [PASS]")

    # Additional verification with empty string edge case logic (though not explicitly requested as a 'distinct' test above, 
    # it's covered by the function implementation. We'll add one more distinct scenario for completeness in output)
    
    print(f"\nTest Case 4 (Empty String):")
    result_empty = swap_adjacent_characters("")
    assert result_empty == "", f"Failed for empty string. Got '{result_empty}'"
    print(f"Input: '' -> Output: '{result_empty}' [PASS]")

    # All tests passed without raising exceptions, indicating correct behavior.