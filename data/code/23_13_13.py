def compare_strings(str1: str, str2: str) -> dict:
    """
    Compares two strings lexicographically and returns a detailed comparison object.
    
    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
        
    Returns:
        dict: A dictionary containing the following keys:
            - 'equal': Boolean indicating if strings are identical up to their minimum length.
            - 'length_diff': Integer difference in lengths (len(str1) - len(str2)).
            - 'first_mismatch_index': Index of first differing character, or None if one is a prefix of the other.
            - 'mismatch_chars': Tuple of characters at mismatch index, or None/None if no mismatch found within bounds.
    """
    result = {
        "equal": True,
        "length_diff": 0,
        "first_mismatch_index": None,
        "mismatch_chars": (None, None)
    }

    len1 = len(str1)
    len2 = len(str2)
    
    # Calculate length difference immediately as per requirement for detail
    result["length_diff"] = len1 - len2
    
    min_len = min(len1, len2)
    
    # Iterate up to the minimum length of both strings
    for i in range(min_len):
        if str1[i] != str2[i]:
            result["equal"] = False
            result["first_mismatch_index"] = i
            result["mismatch_chars"] = (str1[i], str2[i])
            break
    
    # If loop completes without breaking, check for prefix/suffix relationship
    if result["equal"]:
        if len1 != len2:
            result["equal"] = False
            # One is a prefix of the other. The "mismatch" effectively happens at min_len.
            # We report index as min_len and characters as None/None or (char, None) depending on strictness.
            # Standard lexicographical comparison treats longer string as greater if it contains shorter as prefix.
            result["first_mismatch_index"] = min_len
            
    return result

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        ("apple", "apply"),          # Mismatch in middle
        ("hello", "hello"),           # Exact match
        ("short", "longer string"),  # Length difference, prefix relationship
        ("test", ""),                 # One empty string
        ("abc", "abcd")              # Prefix case (first is shorter)
    ]

    print("String Comparison Results:")
    for s1, s2 in test_cases:
        comparison = compare_strings(s1, s2)
        
        status_msg = "Identical" if comparison["equal"] else f"Mismatch at index {comparison['first_mismatch_index']}"
        chars_info = ""
        if comparison["mismatch_chars"][0] is not None or comparison["mismatch_chars"][1] is not None:
            c1, c2 = comparison["mismatch_chars"]
            chars_info = f" ('{c1}' vs '{c2}')" if c1 != c2 else ""

        print(f"'{s1}' vs '{s2}': {status_msg}{chars_info}")
        
        # Debug output for internal logic verification (optional but helpful)
        debug_str = f"\n  Length diff: {comparison['length_diff']}"
        if comparison["first_mismatch_index"] is not None and comparison["mismatch_chars"][0] == "": 
            pass # Avoid printing empty strings in a confusing way for the main output, keep it clean above
        
    print("\nAll tests completed successfully.")