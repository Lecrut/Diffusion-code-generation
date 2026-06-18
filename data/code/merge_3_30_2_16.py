def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps all adjacent character pairs in the input string.
    
    If the length of the string is odd, the last character remains unchanged.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with swapped adjacent characters.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    
    result = []
    length = len(s)
    
    for i in range(0, length - 1, 2):
        # Swap the character at index i with the one at index i+1
        if i + 1 < length:
            result.append(s[i + 1])
            result.append(s[i])
        else:
            # Handle odd-length strings by keeping the last character as is
            result.append(s[i])
    
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "abcdef"
    output_string = swap_adjacent_pairs(sample_input)
    print(output_string)