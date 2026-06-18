def reverse_string(input_str: str) -> str:
    """
    Reverses a given input string efficiently using slicing.
    
    Args:
        input_str (str): The string to be reversed. Can contain any character set, 
                         including empty strings or whitespace-only strings.
        
    Returns:
        str: A new string that is the reverse of the input string.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test edge cases and different character sets
    samples = [
        "",                          # Empty string
        "Hello, World!",            # String with punctuation and spaces
        "Python 3.9",                # String with numbers and dots
        "!@#$%^&*()",               # Special characters only
        "1234567890",               # Digits only
    ]

    for sample in samples:
        reversed_result = reverse_string(sample)
        print(f"Original: '{sample}'")
        print(f"Reversed: '{reversed_result}'\n")