def swap_adjacent_chars(s: str) -> str:
    """
    Swaps all adjacent characters in a string using slicing.
    
    Args:
        s (str): Input string
        
    Returns:
        str: String with adjacent characters swapped
    """
    if len(s) <= 1:
        return s
    
    chars = list(s)
    
    # Swap adjacent elements by iterating in steps of 2 and swapping pairs
    for i in range(0, len(chars), 2):
        j = min(i + 1, len(chars)) - 1
        if i != j:
            chars[i], chars[j] = chars[j], chars[i]
    
    return "".join(chars)

if __name__ == '__main__':
    sample_string = "abcdef"
    result = swap_adjacent_chars(sample_string)
    print(f"Original: {sample_string}")
    print(f"Swapped:  {result}")