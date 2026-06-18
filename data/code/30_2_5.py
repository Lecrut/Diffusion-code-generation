def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps all adjacent character pairs within the input string.
    
    Args:
        s (str): The original string to process.
        
    Returns:
        str: A new string with adjacent characters swapped in each pair.
             Pairs are formed as (s[0], s[1]), (s[2], s[3]), etc.
             If the string length is odd, the last character remains unchanged.
    """
    result = []
    
    # Iterate through the string with a step of 2 to process pairs
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            # Swap current and next characters if both exist
            result.append(s[i + 1])
            result.append(s[i])
        else:
            # Handle odd length string by appending the last character as is
            result.append(s[i])
    
    return ''.join(result)

if __name__ == '__main__':
    sample_strings = [
        "abcdef",
        "a1b2c3d4e5f6g7h8i9j0k"  # Odd length to test edge case
    ]

    for text in sample_strings:
        modified_text = swap_adjacent_pairs(text)
        print(modified_text)