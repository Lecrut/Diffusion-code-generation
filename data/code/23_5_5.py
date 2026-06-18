def compare_strings_and_lengths(s1: str, s2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with 
    (comparison_result, length_difference).
    
    Args:
        s1 (str): The first string.
        s2 (str): The second string.
        
    Returns:
        tuple[int, int]: A tuple containing:
            - comparison_result (int): 0 if equal, 1 if s1 > s2 lexicographically, 
              -1 otherwise.
            - length_difference (int): Length of s1 minus length of s2.
    """
    
    # Calculate the difference in lengths first as it's a straightforward O(1) operation
    len_diff = len(s1) - len(s2)
    
    # Perform lexicographical comparison using built-in string operators which are robust and safe for all characters including non-ASCII (Unicode normalization applies automatically by Python 3 strings). 
    # This handles edge cases like empty strings, Unicode characters correctly.
    if s1 == s2:
        result = 0
    elif s1 > s2:
        result = 1
    else:
        result = -1
        
    return (result, len_diff)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    
    test_cases = [
        ("apple", "banana"),      # Different strings
        ("hello", "world"),       # Different strings
        ("python", "PYTHON"),     # Case sensitive difference (ASCII)
        ("test", "TEST"),         # Case insensitive content but different bytes in Python 3 str comparison? Actually 't' vs 'T'. 
                                  # Note: In ASCII, uppercase letters come before lowercase. So "TEST" < "test".
        ("", ""),                 # Both empty strings (should be equal)
        ("abc", "abcd"),          # Length difference test with prefix match
        
    ]

    for s1_val, s2_val in test_cases:
        result_tuple = compare_strings_and_lengths(s1_val, s2_val)
        comp_res, len_diff = result_tuple
        
        print(f"Comparing '{s1_val}' vs '{s2_val}':")
        print(f"  Lexicographical Result ({comp_res}): {'Equal' if comp_res == 0 else ('Greater' if comp_res > 0 else 'Less')}")
        print(f"  Length Difference: {len_diff}")
        print()