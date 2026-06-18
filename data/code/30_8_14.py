def swap_adjacent_chars(s: str) -> str:
    """
    Swaps adjacent characters in a string, moving from left to right.
    
    The swapping process is iterative: starting at index 0 and 1, 
    if both indices are within the bounds of the string, they are swapped.
    Then it proceeds to indices 2 and 3, then 4 and 5, and so on until 
    an odd index exceeds the length of the string or a pair is found.

    Args:
        s (str): The input string containing characters to be processed.

    Returns:
        str: A new string with adjacent pairs swapped in place.
    
    Examples:
        >>> swap_adjacent_chars("abcd")
        'badc'
        
        >>> swap_adjacent_chars("abcde")
        'bacd e' -> Note: The last character remains as is because there's no pair for it. 
                     Actually, based on the logic of swapping pairs (0-1, 2-3), index 4 stays alone.
                     Let's trace "abcde": indices 0 and 1 swap ('a','b' -> 'b','a'), then 2 and 3 swap ('c','d' -> 'd','c'). 
                     Index 4 is left over. Result: "badce".
    
    Note on odd length strings: The last character, if it exists without a pair (i.e., at an even index in the string where pairs are formed by indices i and i+1), remains unchanged because there is no subsequent character to swap with.
    """
    result = list(s)  # Convert to list for mutability
    
    n = len(result)
    
    # Iterate through the string in steps of 2, swapping elements at index i and i+1 if they exist
    for i in range(0, n - 1, 2):
        result[i], result[i + 1] = result[i + 1], result[i]
        
    return ''.join(result)

if __name__ == '__main__':
    # Test Case 1: String of even length (4 characters)
    test_even_length_input = "abcd"
    expected_output_1 = "badc"
    
    actual_output_1 = swap_adjacent_chars(test_even_length_input)
    assert actual_output_1 == expected_output_1, f"Test 1 Failed: Expected '{expected_output_1}', got '{actual_output_1}'"

    # Test Case 2: String of odd length (5 characters)
    test_odd_length_input = "abcde"
    expected_output_2 = "badce"
    
    actual_output_2 = swap_adjacent_chars(test_odd_length_input)
    assert actual_output_2 == expected_output_2, f"Test 2 Failed: Expected '{expected_output_2}', got '{actual_output_2}'"

    # Test Case 3: String of even length (6 characters) with repeated chars to verify logic robustness
    test_even_length_input_long = "abcdefg"[:-1]  # Slicing ensures exactly 6 chars -> "abcde f" without space, just "abcdef"
    expected_output_3 = "bacdef"
    
    actual_output_3 = swap_adjacent_chars("abcdef")
    assert actual_output_3 == expected_output_3, f"Test 3 Failed: Expected '{expected_output_3}', got '{actual_output_3}'"

    print("All tests passed successfully.")