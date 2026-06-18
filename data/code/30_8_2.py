def swap_adjacent_chars(s: str) -> str:
    """
    Swaps adjacent characters in a string, moving from left to right.
    
    If the string has an even length (n), pairs are formed as (0,1), (2,3), ..., (n-2,n-1).
    Each pair is swapped in place before processing the next.
    
    If the string has an odd length (n), all full adjacent pairs up to index n-3 
    are processed; the final character at index n-1 remains unchanged as it cannot form a pair.
    
    Parameters:
        s (str): The input string containing only characters (no whitespace required, but supported).
        
    Returns:
        str: A new string with adjacent pairs swapped in place. Unchanged if length is 0 or 1.

    Examples:
        >>> swap_adjacent_chars("abcd") -> "badc"
        >>> swap_adjacent_chars("abcde") -> "bacde" (last char 'e' remains)
        
    Note: This function creates a new string and does not modify the input in place.
    """
    if len(s) <= 1:
        return s
    
    result = []
    
    # Iterate over indices with step of 2 to form pairs (i, i+1)
    for i in range(0, len(s), 2):
        next_idx = i + 1
        
        # If there is a second character available, swap and add both; otherwise just append the last one
        if next_idx < len(s):
            result.append(s[next_idx])
            result.append(s[i])
        else:
            # Odd length case for the very last char (should not happen in logic flow since loop steps by 2)
            # But added defensively. If i is odd and no pair exists, append it alone? 
            # Actually per spec "adjacent characters", so if we have 'abc' -> swap a,b then c stays.
            result.append(s[i])

    return "".join(result)

if __name__ == '__main__':
    # Test Case 1: Even length string ("abcd") - expected output should be "badc"
    test_str_1 = "abcd"
    assert swap_adjacent_chars(test_str_1) == "badc", f"Test 1 failed. Expected 'badc', got '{swap_adjacent_chars(test_str_1)}'"

    # Test Case 2: Odd length string ("abcde") - expected output should be "bacde" (last char unchanged)
    test_str_2 = "abcde"
    assert swap_adjacent_chars(test_str_2) == "bacde", f"Test 2 failed. Expected 'bacde', got '{swap_adjacent_chars(test_str_2)}'"

    # Test Case 3: Single character string ("z") - expected output should be unchanged "z"
    test_str_3 = "z"
    assert swap_adjacent_chars(test_str_3) == "z", f"Test 3 failed. Expected 'z', got '{swap_adjacent_chars(test_str_3)}'"

    print("All tests passed successfully.")