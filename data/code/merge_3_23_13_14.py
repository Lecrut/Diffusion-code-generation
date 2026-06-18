def compare_strings(str1: str, str2: str) -> dict:
    """
    Compares two strings lexicographically.
    
    Returns a dictionary containing:
        - 'is_equal': bool indicating if strings are identical
        - 'min_length': int length of the shorter string
        - 'max_length': int length of the longer string
        - 'length_difference': int difference (positive, negative or zero)
        - 'first_diff_index': index of first differing character (-1 if no diff before end)
    """
    is_equal = True
    
    # Determine lengths
    len1 = len(str1)
    len2 = len(str2)
    
    min_length = min(len1, len2)
    max_length = max(len1, len2)
    length_difference = max_length - min_length
    
    first_diff_index = -1  # No difference found yet
    
    # Iterate up to the length of the shorter string
    for i in range(min_length):
        if str1[i] != str2[i]:
            is_equal = False
            first_diff_index = i
            break
            
    return {
        'is_equal': is_equal,
        'min_length': min_length,
        'max_length': max_length,
        'length_difference': length_difference,
        'first_diff_index': first_diff_index
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    
    test_cases = [
        ("apple", "banana"),
        ("hello world", "hellosunrise"),
        ("abc", "ab"),
        ("xyz", "zyx"),
        ("identical here!", "identical here!"),
        "", "",
        ("a" * 10, "b" * 5),
    ]
    
    print("String Comparison Results:\n")
    for s1, s2 in test_cases:
        result = compare_strings(s1, s2)
        
        # Format output clearly
        diff_status = "Matched exactly!" if result['is_equal'] else f"Differ at index {result['first_diff_index']}"
        
        print(f"Comparing '{s1}' and '{s2}':")
        print(f"  Lengths: Short={result['min_length']}, Long={result['max_length']}")
        print(f"  Difference ({len(s1)} vs {len(s2)}) = +{result['length_difference']} to longer string\n", end="")

    # Verify no external inputs were used by checking the output was generated directly from hardcoded data above