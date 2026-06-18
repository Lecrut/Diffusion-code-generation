def compare_strings_lexicographically(s1: str, s2: str) -> dict:
    """
    Compares two strings lexicographically and returns a detailed comparison object.
    
    Args:
        s1 (str): First string to compare.
        s2 (str): Second string to compare.
        
    Returns:
        dict: A dictionary containing the following keys:
            - 'length_diff': Integer difference in length between s2 and s1 (s2_len - s1_len).
            - 'first_differ_index': Index of the first differing character (-1 if one string is a prefix of another or both are identical).
            - 'match_up_to_index': The index up to which strings match exactly.
    """
    
    # Calculate length difference (s2 minus s1)
    length_diff = len(s2) - len(s1)
    
    # Determine the minimum length for character-by-character comparison
    min_len = min(len(s1), len(s2))
    
    # Find the first differing index or determine if one is a prefix of another
    match_up_to_index = 0
    
    while match_up_to_index < min_len:
        char_s1 = s1[match_up_to_index]
        char_s2 = s2[match_up_to_index]
        
        # Check for lexicographical inequality at current index
        if char_s1 != char_s2:
            first_differ_index = match_up_to_index
            
            break  # Exit loop as we found the difference
        
        # Increment index to check next character
        match_up_to_index += 1
    
    else:
        # If loop completes without breaking, strings are identical up to min_len.
        if len(s1) == len(s2):
            first_differ_index = -1  # Identical strings
        
        elif s1.startswith(s2) or s2.startswith(s1):
            # Handle prefix cases: the "difference" is effectively at the end of the longer string
            # However, based on standard lexicographical comparison logic where shorter non-identical 
            # prefixes come before longer ones (e.g., 'a' < 'aa'), we return -2 to indicate no character mismatch
            # but a length difference exists that determines order.
            first_differ_index = -1  # No differing character, one is prefix of another
            
    comparison_result = {
        "length_diff": length_diff,
        "first_differ_index": first_differ_index,
        "match_up_to_index": match_up_to_index
    }
    
    return comparison_result

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    test_cases = [
        ("python", "pythons"),       # Prefix case: s1 is prefix of s2
        ("banana", "bandana"),      # Character mismatch at index 3 ('n' vs 'd')
        ("hello", "world"),          # Mismatch at first character (index 0)
        ("abcde", "abcd")            # Suffix case: s1 is prefix of longer string, actually s2 is prefix here? No. 
                                     # Here s1="abcde", s2="abcd". Match up to index 4 ('e' vs nothing).
                                     # Logic above handles this via min_len loop termination and prefix check.
    ]

    for i, (s_a, s_b) in enumerate(test_cases):
        result = compare_strings_lexicographically(s_a, s_b)
        
        print(f"\n--- Test Case {i + 1} ---")
        print(f"String A: '{s_a}'")
        print(f"String B: '{s_b}'")
        print("Comparison Result:")
        for key in ["length_diff", "first_differ_index", "match_up_to_index"]:
            if result[key] is not None or isinstance(result[key], int): # Ensure we don't print weird types if logic changes, though here all are ints/None-like -1/-2
                print(f"  {key}: {result[key]}")
        
        # Additional validation for specific cases to ensure robustness in output interpretation
        is_prefix = s_a.startswith(s_b) or s_b.startswith(s_a) and len(result["match_up_to_index"]) == min(len(s_a), len(s_b)) if not (s_a == s_b) else False
        
        print(f"  Note: 'A' starts with B? {s_a.startswith(s_b)}")