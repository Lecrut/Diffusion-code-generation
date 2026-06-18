def reverse_string(input_str: str) -> str:
    """
    Reverses a given input string efficiently using slicing.
    
    Args:
        input_str (str): The string to be reversed. Can handle any character set, 
                         including empty strings and Unicode characters.
        
    Returns:
        str: A new string that is the reverse of the input string.
            
    Examples:
        >>> reverse_string("Hello")
        'olleH'
        >>> reverse_string("")
        ''
        >>> reverse_string("你好世界")
        '界世好你'
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    test_cases = [
        "Hello, World!",  # Standard string with spaces and punctuation
        "",               # Empty string edge case
        "!@#$%^&*()",     # Special characters
        "12345",          # Numeric digits only
        "你好世界！🌍"    # Unicode text including emojis
    ]

    for test_input in test_cases:
        reversed_result = reverse_string(test_input)
        print(f"Original: '{test_input}'")
        print(f"Reversed: '{reversed_result}'\n")