def reverse_string(s: str) -> str:
    """
    Reverses a given input string efficiently.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing various edge cases and character sets
    samples = [
        "",                      # Empty string
        "a",                     # Single character
        "Hello, World!",         # String with punctuation and spaces
        "!@#$%",                 # Special characters
        "12345 67890",           # Numbers and mixed whitespace
    ]

    for sample in samples:
        result = reverse_string(sample)
        print(f"Original: {sample!r}")
        print(f"Reversed: {result!r}\n")