def swap_adjacent_chars(s: str) -> str:
    """
    Swaps adjacent characters in a string two at a time.
    
    If the string has an odd length, the last character remains unchanged 
    as there is no pair for it to be swapped with.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped.
        
    Examples:
        >>> swap_adjacent_chars("abcd")
        'badc'
        >>> swap_adjacent_chars("abcde")
        'bacde'
        >>> swap_adjacent_chars("")
        ''
    """
    if not s:
        return ""
    
    result = []
    i = 0
    
    while i < len(s):
        # Append the character at current index
        result.append(s[i])
        
        # If there is a next character, swap it with the one we just added
        if i + 1 < len(s):
            result.insert(1, s[i + 1])
            
        # Move to the next pair start (step by 2)
        i += 2
        
    return "".join(result)

if __name__ == '__main__':
    # Test case 1: Even length string ("abcd") -> Expected "badc"
    test_str_1 = "abcd"
    expected_result_1 = "badc"
    
    # Test case 2: Odd length string ("abcde") -> Expected "bacde" (last char stays)
    test_str_2 = "abcde"
    expected_result_2 = "bacde"
    
    # Test case 3: Empty string "" -> Expected ""
    test_str_3 = ""
    expected_result_3 = ""

    print(f"Test Case 1 (Even length):")
    result_1 = swap_adjacent_chars(test_str_1)
    assert result_1 == expected_result_1, f"Failed: '{result_1}' != '{expected_result_1}'"
    print(f"Input: {test_str_1}")
    print(f"Output: {result_1} (Expected: {expected_result_1})")
    
    print("\nTest Case 2 (Odd length):")
    result_2 = swap_adjacent_chars(test_str_2)
    assert result_2 == expected_result_2, f"Failed: '{result_2}' != '{expected_result_2}'"
    print(f"Input: {test_str_2}")
    print(f"Output: {result_2} (Expected: {expected_result_2})")

    print("\nTest Case 3 (Empty string):")
    result_3 = swap_adjacent_chars(test_str_3)
    assert result_3 == expected_result_3, f"Failed: '{result_3}' != '{expected_result_3}'"
    print(f"Input: {test_str_3}")
    print(f"Output: {result_3} (Expected: {expected_result_3})")

    print("\nAll tests passed successfully.")