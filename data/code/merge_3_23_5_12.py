def robust_string_compare(s1: str, s2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with 
    (comparison_result, length_difference).
    
    Args:
        s1 (str): The first string to compare.
        s2 (str): The second string to compare.
        
    Returns:
        tuple[int, int]: A tuple containing two integers:
            - comparison_result (-1 if s1 < s2 lexicographically, 
                          0 if equal, or 1 if s1 > s2)
            - length_difference (int): s1_length - s2_length
    
    Raises:
        TypeError: If either input is not a string.
    """
    # Validate inputs are strings
    if not isinstance(s1, str):
        raise TypeError(f"Expected 'str' for first argument, got {type(s1).__name__}")
    
    if not isinstance(s2, str):
        raise TypeError(f"Expected 'str' for second argument, got {type(s2).__name__}")

    # Perform lexicographical comparison using standard string operators
    cmp_result = -1 if s1 < s2 else 0
    
    # If the strings are equal up to one of them's length (lexicographically), 
    # but their lengths differ, we need a specific tie-breaker. 
    # However, Python's default '<' operator handles lexicographical order fully
    # based on character codes and implicitly considers shorter string as smaller
    # if it is a prefix of the longer one. The standard comparison covers all cases.

    length_diff = len(s1) - len(s2)
    
    return cmp_result, length_diff

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input
    
    # Sample 1: Different characters and lengths
    result_a, diff_a = robust_string_compare("apple", "banana")
    
    # Sample 2: One string is a prefix of the other ("app" vs "apple")
    result_b, diff_b = robust_string_compare("app", "apple")
    
    # Sample 3: Identical strings
    result_c, diff_c = robust_string_reverse("", "")

    print(f"Sample 1 ('apple', 'banana'): Comparison={result_a}, Len Diff={diff_a}")