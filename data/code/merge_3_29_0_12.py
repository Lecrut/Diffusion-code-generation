def reverse_string(input_str: str) -> str:
    """
    Reverses a given input string efficiently using slicing.
    
    Args:
        input_str (str): The string to be reversed. Handles empty strings, 
                         Unicode characters, and mixed character sets correctly.
        
    Returns:
        str: A new string with the characters in reverse order.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test edge cases without user interaction
    samples = [
        "",                      # Empty string
        "hello",                 # Standard lowercase letters
        "Hello, World!",         # Mixed case and punctuation
        "🌍 123 🎉",             # Unicode characters and numbers
        "!@#$%",                  # Special symbols only
    ]

    for sample in samples:
        reversed_result = reverse_string(sample)
        print(f"Original: '{sample}'")
        print(f"Reversed: '{reversed_result}'\n")