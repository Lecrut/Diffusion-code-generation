def reverse_word(s: str) -> str:
    """
    Returns a new string with characters in 's' reversed.
    Uses slicing which is the most Pythonic and efficient method.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string containing the characters of 's' in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Sample values that run without user input or external dependencies
    test_cases = [
        "Hello, World!",
        "Python",
        "",
        "a"
    ]

    for original in test_cases:
        reversed_str = reverse_word(original)
        print(f"Original: '{original}'")
        print(f"Reversed: '{reversed_str}'\n")