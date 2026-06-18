def reverse_adjacent_swaps(s: str) -> str:
    """
    Swaps every pair of adjacent characters in the string.
    
    For example, if input is "abcd", output will be "bacd".
    If input length is odd (e.g., "abc"), only the first two are swapped ("bac").
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with every pair of adjacent characters swapped.
    """
    # Convert list to avoid modifying original while iterating safely if needed, 
    # but since we're building a result from scratch via slicing or accumulation,
    # direct construction is fine for O(n). Using slice concatenation approach.
    
    length = len(s)
    result_chars = []

    i = 0
    while i < length:
        if i + 1 < length:
            # Swap current and next character
            result_chars.append(s[i+1])
            result_chars.append(s[i])
            i += 2
        else:
            # Handle odd-length string, last char remains as is (no pair)
            result_chars.append(s[i])
            break
            
    return ''.join(result_chars)

if __name__ == '__main__':
    sample1 = "abcdef"
    expected1 = "bacfed"
    
    sample2 = "abcd"
    expected2 = "bacd"
    
    sample3 = "a"
    expected3 = "a"
    
    # Test cases to verify correctness without user input or external dependencies
    assert reverse_adjacent_swaps(sample1) == expected1, f"Test 1 failed: {reverse_adjacent_swaps(sample1)} != {expected1}"
    assert reverse_adjacent_swaps(sample2) == expected2, f"Test 2 failed: {reverse_adjacent_swaps(sample2)} != {expected2}"
    assert reverse_adjacent_swaps(sample3) == expected3, f"Test 3 failed: {reverse_adjacent_swaps(sample3)} != {expected3}"

    print("All tests passed.")
    
    # Additional demonstration prints for clarity (optional but helpful without violating constraints)
    demo_cases = ["hello", "123456789"]
    for case in demo_cases:
        swapped_case = reverse_adjacent_swaps(case)
        print(f"Input: '{case}' -> Output: '{swapped_case}'")