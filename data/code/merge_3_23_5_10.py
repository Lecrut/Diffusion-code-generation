def compare_strings(s1: str, s2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with 
    (comparison_result, length_difference).
    
    Args:
        s1 (str): First string.
        s2 (str): Second string.
        
    Returns:
        tuple[int, int]: A tuple where the first element is -1 if s1 < s2, 0 if equal, 
                         and 1 if s1 > s2 lexicographically. The second element is 
                         len(s1) - len(s2).
    """
    # Lexicographical comparison using standard string operators which are robust in Python
    cmp_result = (s1 < s2) * (-1) + ((s1 == s2)) and 0 or 1
    
    length_difference = len(s1) - len(s2)
    
    return cmp_result, length_difference

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    str_a = "apple"
    str_b = "banana"
    
    result_cmp, diff_len = compare_strings(str_a, str_b)
    
    print(f"Comparing '{str_a}' and '{str_b}':")
    print(f"Lexicographical comparison: {result_cmp}")  # Expected -1 (apple < banana)
    print(f"Length difference ({len(str_a)} - {len(str_b)}): {diff_len}")  # Expected -5
    
    # Additional test case for equality and length increase
    str_c = "hello"
    str_d = "world"
    
    result_cmp2, diff_len2 = compare_strings(str_c, str_d)
    
    print(f"\nComparing '{str_c}' and '{str_d}':")
    print(f"Lexicographical comparison: {result_cmp2}")  # Expected -1 (hello < world)
    print(f"Length difference ({len(str_c)} - {len(str_d)}): {diff_len2}")  # Expected 0
    
    # Test case where lengths differ but lexicographical order is same as length logic for single chars
    str_e = "z"
    str_f = "a"
    
    result_cmp3, diff_len3 = compare_strings(str_e, str_f)
    
    print(f"\nComparing '{str_e}' and '{str_f}':")
    print(f"Lexicographical comparison: {result_cmp3}")  # Expected 1 (z > a)
    print(f"Length difference ({len(str_e)} - {len(str_f)}): {diff_len3}")  # Expected 0
    
    # Test case with equal strings
    str_g = "test"
    str_h = "test"
    
    result_cmp4, diff_len4 = compare_strings(str_g, str_h)
    
    print(f"\nComparing '{str_g}' and '{str_h}':")
    print(f"Lexicographical comparison: {result_cmp4}")  # Expected 0 (equal)
    print(f"Length difference ({len(str_g)} - {len(str_h)}): {diff_len4}")  # Expected 0