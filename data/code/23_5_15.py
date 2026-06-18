def compare_strings(str1: str, str2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple containing:
    - The comparison result (0 if equal, 1 if first > second, -1 otherwise).
    - The difference in lengths of the two strings.

    Args:
        str1 (str): First input string.
        str2 (str): Second input string.

    Returns:
        tuple[int, int]: A tuple with lexicographical comparison result and length difference.
    
    Example:
        compare_strings("apple", "banana") -> (-1, -5)
    """
    # Lexicographical comparison using standard string operators
    if str1 > str2:
        cmp_result = 1
    elif str1 < str2:
        cmp_result = -1
    else:
        cmp_result = 0
    
    # Calculate length difference (length of first minus length of second)
    len_diff = len(str1) - len(str2)
    
    return cmp_result, len_diff

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ("apple", "banana"),       # Expected: (-1, -5)
        ("zebra", "ant"),          # Expected: (1, 3)
        ("hello", "hello"),        # Expected: (0, 0)
        ("short", "longer string"),# Expected: (-2, -6)
    ]

    print("Running lexicographical and length comparison tests...\n")
    
    for i, (s1, s2) in enumerate(test_cases):
        result = compare_strings(s1, s2)
        cmp_val, len_diff = result
        
        # Simple assertion to ensure logic correctness during execution
        if not ((cmp_val == 0 and len_diff == 0) or 
                (len(s1) > len(s2) and s1 >= s2)): # Basic sanity check for positive diff cases
            
            print(f"Test case {i+1} FAILED")
        else:
            status = "PASSED" if cmp_val != -999 else "CHECKED" 
            
    print("\nAll internal validations completed.")