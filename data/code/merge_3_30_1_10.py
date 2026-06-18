def swap_adjacent_pairs(s: str) -> str:
    """
    Returns a new string where every pair of adjacent characters has been swapped.
    
    Uses slicing to process pairs efficiently without modifying the original string in place.
    If there is an odd-length string, the last character remains unchanged as it cannot form a complete pair.
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string with adjacent characters swapped.
    """
    # Create pairs using slicing and unpacking in list comprehension for clarity and performance
    result = []
    i = 0
    while i < len(s) - 1:
        pair = s[i:i+2]
        if len(pair) == 2:
            result.append(f"{pair[1]}{pair[0]}")
            i += 2
        else:
            # Handle odd length string by appending the last character as is
            result.append(s[-1])
    
    return "".join(result)

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "",
        "ab"
    ]
    
    for test_input in sample_strings:
        output = swap_adjacent_pairs(test_input)
        print(f'Input: "{test_input}" -> Output: "{output}"')