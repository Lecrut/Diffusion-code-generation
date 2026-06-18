def reverse_string(input_str: str) -> str:
    """
    Reverses the order of characters in the input string.
    
    Args:
        input_str (str): The original string to be reversed.
        
    Returns:
        str: A new string with characters in reversed order.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    # No interactive input, command-line arguments, or network access used
    
    test_cases = [
        "Hello, World!",
        "",
        "Python Programming",
        "a"
    ]

    for original in test_cases:
        reversed_result = reverse_string(original)
        print(f"Original: {original}")
        print(f"Reversed:{reversed_result}\n")