def reverse_word(s: str) -> str:
    """
    Returns the reversed version of the input string.
    
    Args:
        s (str): The original string to be reversed.
        
    Returns:
        str: A new string with characters in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    samples = ["hello", "world", "Python3"]
    
    for sample in samples:
        print(f"Original: {sample} -> Reversed: {reverse_word(sample)}")