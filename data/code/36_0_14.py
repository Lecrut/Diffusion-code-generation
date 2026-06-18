def reverse_string(input_str: str) -> str:
    """
    Reverses the order of characters in a given string.
    
    Args:
        input_str (str): The string to be reversed.
        
    Returns:
        str: A new string with characters in reverse order.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_cases = [
        "Hello, World!",
        "Python Programming",
        "",
        "a"
    ]

    for text in test_cases:
        reversed_text = reverse_string(text)
        print(f"Original: '{text}'")
        print(f"Reversed: '{reversed_text}'\n")