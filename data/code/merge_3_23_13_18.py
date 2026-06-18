def compare_strings(s1: str, s2: str) -> dict:
    """
    Compares two strings lexicographically and returns a detailed comparison object.
    
    Args:
        s1 (str): The first string to compare.
        s2 (str): The second string to compare.
        
    Returns:
        dict: A dictionary containing the length difference, index of the first differing character, 
              whether strings are equal, and a list of characters up to the point of divergence or end.
    
    Raises:
        TypeError: If either input is not a string.
    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Both arguments must be strings.")

    min_len = min(len(s1), len(s2))
    max_len = max(len(s1), len(s2))
    
    comparison_result = {
        'length_difference': abs(len(s1) - len(s2)),
        'longer_string_length': max_len,
        'shorter_string_length': min_len,
        'is_equal': s1 == s2,
        'first_differing_index': None,
        'prefix_match_chars': [],
        'excess_chars_in_s1': [] if len(s1) > len(s2) else [None], # Placeholder for potential logic extension
        'excess_chars_in_s2': [] if len(s2) > len(s1) else [None]
    }

    found_difference = False
    
    for i in range(min_len):
        comparison_result['prefix_match_chars'].append((s1[i], s2[i]))
        
        # Check lexicographical difference at this index (ignoring case as per standard string operations unless specified)
        if s1[i] != s2[i]:
            comparison_result['first_differing_index'] = i
            found_difference = True
            break

    # If no difference was found within the shorter length, check for different lengths
    if not found_difference:
        if len(s1) > min_len and len(s2) == min_len:
            comparison_result['first_differing_index'] = min_len
            excess_chars_in_s1 = list(s1[min_len:])
            comparison_result['excess_chars_in_s1'] = excess_chars_in_s1
            
        elif len(s2) > min_len and len(s1) == min_len:
            comparison_result['first_differing_index'] = min_len
            excess_chars_in_s2 = list(s2[min_len:])
            comparison_result['excess_chars_in_s2'] = excess_chars_in_s2

    return comparison_result

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    
    sample_data_1 = ("Hello World", "HelloWorld")
    sample_data_2 = ("Python 3.9", "python 3.8")
    sample_data_3 = ("Test Case", "Test Case")