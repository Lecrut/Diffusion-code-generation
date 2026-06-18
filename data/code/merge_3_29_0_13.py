def reverse_string(input_str: str) -> str:
    """
    Reverses a given input string efficiently using slicing.
    
    Args:
        input_str (str): The string to be reversed. Can contain any character set, 
                         including empty strings or Unicode characters.
        
    Returns:
        str: A new string that is the reverse of the input string.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test edge cases and different character sets
    samples = [
        "",                          # Empty string
        "hello",                     # Simple lowercase word
        "Hello, World!",             # Mixed case with punctuation
        "1234567890",                # Digits only
        "你好世界",                   # Unicode Chinese characters
    ]

    for sample in samples:
        reversed_str = reverse_string(sample)
        print(f"Original: '{sample}'")
        print(f"Reversed: '{reversed_str}'\n")