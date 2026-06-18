def reverse_string(input_str: str) -> str:
    """
    Reverses the order of characters in the input string.
    
    Args:
        input_str (str): The original string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "Hello, World!",
        "",
        "a",
        "Python scripting is fun!"
    ]

    print("Reversed String Examples:")
    for original in test_cases:
        reversed_str = reverse_string(original)
        print(f"Original: '{original}'")
        print(f"Reversed: '{reversed_str}'\n")