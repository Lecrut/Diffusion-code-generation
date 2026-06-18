def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps all adjacent character pairs in a string.
    
    If the string length is odd, the last single character remains unchanged.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with swapped adjacent characters.
    """
    if len(s) == 0:
        return s
    
    result = []
    i = 0
    length = len(s)
    
    while i < length - 1:
        # Swap the current character and the next one
        pair = list(s[i:i+2])
        pair.reverse()
        result.extend(pair)
        i += 2
    
    # If there's a remaining single character at the end, append it as is
    if length % 2 == 1:
        result.append(s[length - 1])
    
    return ''.join(result)

if __name__ == '__main__':
    sample_strings = [
        "abcdef",
        "aabbccdd",
        "python"
    ]
    
    for test_input in sample_strings:
        output_string = swap_adjacent_pairs(test_input)
        print(output_string)