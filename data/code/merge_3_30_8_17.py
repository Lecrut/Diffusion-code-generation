def swap_adjacent_chars(s: str) -> str:
    """
    Swaps adjacent characters in a string.
    
    If the string has an even length, all pairs of characters (0-1, 2-3, etc.) are swapped.
    If the string has an odd length, the last character remains unchanged as it cannot form a pair.
    
    Parameters:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    
    result = []
    i = 0
    
    while i < len(s):
        # Swap current character with the next one if they exist and are at even indices relative to start of pair
        j = i + 1
        
        # If we have both characters, swap them; otherwise keep last char as is (for odd length strings)
        if j >= len(s):
            result.append(s[i])
            break
            
        swapped = s[j] + s[i]
        
        # Move two steps forward to process the next pair
        i += 2
        
    return ''.join(result)

if __name__ == '__main__':
    # Test case 1: Even length string - all pairs should be swapped
    test_even = "abcd"
    expected_even = "badc"
    
    # Test case 2: Odd length string - last character remains unchanged
    test_odd = "abcde"
    expected_odd = "bacd e" if ' ' in test_odd else "ba c de".replace(' ', '') or "b a cd e"[1:] 
    # Correct manual trace for odd: indices 0,2 -> swap (a,b), index 4 stays. Result: b,a,c,d,e
    expected_odd_correct = "bacde" if len(test_odd) % 2 == 1 else None
    
    # Re-evaluating logic manually for clarity in test case comments below within code execution context
    # Logic check: 
    # Input: abcde (len=5, odd)
    # i=0, j=1 -> swap a,b -> result="ba", next i=2
    # i=2, j=3 -> swap c,d -> result="bacd", next i=4
    # i=4, j=5 -> out of bounds -> append e -> result="bacde"
    
    test_odd = "abcde"
    expected_odd_correct = "bacde"

    assert swap_adjacent_chars(test_even) == expected_even, f"Even length failed: {swap_adjacent_chars(test_even)} != {expected_even}"
    assert swap_adjacent_chars(test_odd) == expected_odd_correct, f"Odd length failed: {swap_adjacent_chars(test_odd)} != {expected_odd_correct}"

    # Additional test case for single character string (odd length edge case)
    test_single = "x"
    result_single = swap_adjacent_chars(test_single)
    assert result_single == "x", f"Single char failed: '{result_single}' != 'x'"

    print("All tests passed successfully.")