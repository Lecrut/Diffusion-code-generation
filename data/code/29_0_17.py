def reverse_string(input_str: str) -> str:
    """
    Reverses a given input string efficiently using slicing.
    
    Args:
        input_str (str): The string to be reversed.
        
    Returns:
        str: A new string that is the reverse of the input string.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing edge cases and different character sets
    test_cases = [
        "",                          # Empty string
        "a",                         # Single character
        "Python programming is fun!",  # Sentence with punctuation and spaces
        "!_@#$%^&*() ",               # Special characters and trailing space
        "1234567890",                # Digits only
    ]

    for test_input in test_cases:
        result = reverse_string(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{result}'\n")