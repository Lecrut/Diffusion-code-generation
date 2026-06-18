def reverse_adjacent_swaps(s: str) -> str:
    """
    Swaps every pair of characters in the input string.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent pairs swapped.
    """
    # Convert string to a list for mutability, then swap and join back
    chars = list(s)
    n = len(chars)
    
    # Iterate through the characters in steps of 2 up to an even number (n-1 if odd length)
    i = 0
    while i < n - 1:
        # Swap current character with next one
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
        i += 2
        
    return ''.join(chars)

if __name__ == '__main__':
    sample_strings = [
        "abcdef",
        "python3.9",
        "a"
    ]

    for test_input in sample_strings:
        result = reverse_adjacent_swaps(test_input)
        print(f"Input: '{test_input}' -> Output: '{result}'")