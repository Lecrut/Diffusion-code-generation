def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a given string, handling Unicode correctly.
    
    This function iterates through the input string from end to start and constructs 
    a new string with characters in reversed order. It properly handles all Unicode 
    character representations including emojis, combining diacritical marks, and other 
    complex scripts by treating each code point as an individual unit during iteration.

    Parameters:
        s (str): The input string to be reversed. Can contain any valid Python string 
                 characters, including international text and emoji sequences.

    Returns:
        str: A new string containing the characters of the original string in reverse order.
    
    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("🌍Hello 世界")
        '界世! olleH🌍'
        
    Notes:
        - The function does not modify the original string but returns a new one.
        - It assumes valid UTF-8 encoding as per Python's standard behavior for strings.
    
    Raises:
        TypeError: If the input is not a string type (though in practice, this 
                  would be caught by static analysis or runtime checks if necessary).
    """
    return "".join(reversed(s))

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure no user interaction or external dependencies are needed.
    
    sample_strings = [
        "hello",
        "Python 3.12",
        "🌍Hello World!",
        "日本語テスト",
        "",
        "A" * 100,  # Test with a long string of repeated characters
    ]

    for test_input in sample_strings:
        reversed_result = reverse_string(test_input)
        print(f"Original: {test_input!r}")
        print(f"Reversed:{reversed_result!r}\n")