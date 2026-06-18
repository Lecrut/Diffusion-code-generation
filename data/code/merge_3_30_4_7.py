def reverse_adjacent_swaps(s: str) -> str:
    """
    Swaps every pair of adjacent characters in the string.
    
    Logic: Iterates through the string with a step of 2, swapping 
            the character at index i with index i+1 if both exist.
    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(1) auxiliary (excluding output space).
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with every adjacent pair swapped.
    """
    # Convert string to list for mutability, then swap pairs and join back
    chars = list(s)
    length = len(chars)
    
    i = 0
    while i < length - 1:
        # Swap characters at current index (i) and next index (i+1)
        if i + 1 < length:
            temp_char = chars[i]
            chars[i] = chars[i + 1]
            chars[i + 1] = temp_char
        
        # Move to the next pair start, stepping by 2 indices
        i += 2
    
    return ''.join(chars)

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    sample_inputs = [
        "abcdef",
        "",
        "ab",
        "a",
        "12345678"
    ]

    for test_string in sample_inputs:
        result = reverse_adjacent_swaps(test_string)
        print(f'Input: "{test_string}" -> Output: "{result}"')