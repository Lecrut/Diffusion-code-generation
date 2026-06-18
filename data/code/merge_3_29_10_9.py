def reverse_string(input_str: str) -> str:
    """
    Reverses a given input string.
    
    Args:
        input_str (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    # No user interaction, command-line arguments, or network access is used
    
    test_cases = [
        "Hello World",
        "",
        "Python Programming",
        "!@#$%",
        "12345"
    ]

    for original in test_cases:
        reversed_str = reverse_string(original)
        print(f"Original: '{original}'")
        print(f"Reversed: '{reversed_str}'\n")