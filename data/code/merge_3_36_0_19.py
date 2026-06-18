def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a given string.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string with characters in reversed order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    test_cases = [
        "Hello, World!",
        "",
        "Python",
        "a"
    ]

    for original in test_cases:
        reversed_str = reverse_string(original)
        print(f"Original: '{original}'")
        print(f"Reversed: '{reversed_str}'\n")