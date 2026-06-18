def reverse_word(text: str) -> str:
    """
    Reverses a single string using slicing for maximum efficiency.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: A new string containing the characters of the original string in reverse order.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = ["hello", "Python programming", "!HolB", ""]
    
    for s in samples:
        print(f"Original: '{s}' -> Reversed: '{reverse_word(s)}'")