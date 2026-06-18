def swap_adjacent_chars(s: str) -> str:
    """
    Swaps adjacent characters in a string two at a time, moving from left to right.
    
    If the string has an odd length, the last character remains unchanged as it 
    cannot be paired with another character after its index is reached.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped where possible.
             Unpaired characters in odd-length strings are left at their original positions.
             
    Examples:
        >>> swap_adjacent_chars("ab")
        'ba'
        >>> swap_adjacent_chars("abcd")
        'badc'
        >>> swap_adjacent_chars("abc")
        'bac'
    """
    if not s:
        return ""
    
    result = list(s)
    length = len(result)
    
    # Iterate through the string in steps of 2, swapping elements at index i and i+1
    for i in range(0, length - 1, 2):
        if i + 1 < length:
            result[i], result[i + 1] = result[i + 1], result[i]
            
    return "".join(result)

if __name__ == '__main__':
    # Test case 1: Even length string (length 4)
    test_even_1 = "abcd"
    expected_result_1 = "badc"
    
    # Test case 2: Odd length string (length 3), last char remains fixed relative to swap logic
    test_odd = "abc"
    expected_result_odd = "bac"
    
    # Test case 3: Even length string with repeated characters for clarity
    test_even_2 = "aabbccdd"
    expected_result_2 = "bbaaccdd"

    print(f"Test Case 1 (Even Length 'abcd'): Expected '{expected_result_1}', Got '{swap_adjacent_chars(test_even_1)}'")
    assert swap_adjacent_chars(test_even_1) == expected_result_1, f"Failed for {test_even_1}"

    print(f"Test Case 2 (Odd Length 'abc'): Expected '{expected_result_odd}', Got '{swap_adjacent_chars(test_odd)}'")
    assert swap_adjacent_chars(test_odd) == expected_result_odd, f"Failed for {test_odd}"

    print(f"Test Case 3 (Even Length 'aabbccdd'): Expected '{expected_result_2}', Got '{swap_adjacent_chars(test_even_2)}'")
    assert swap_adjacent_chars(test_even_2) == expected_result_2, f"Failed for {test_even_2}"

    print("All tests passed successfully.")