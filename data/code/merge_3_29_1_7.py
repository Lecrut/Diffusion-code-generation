def reverse_word(s: str) -> str:
    """
    Returns the reversed version of a single string argument.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    sample_strings = ["hello", "Python programming"]
    
    for text in sample_strings:
        print(f"Original: {text}")
        print(f"Reversed: {reverse_word(text)}")