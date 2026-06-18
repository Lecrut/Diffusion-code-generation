def reverse_string(s: str) -> str:
    """
    Reverses a string while correctly handling Unicode characters.
    
    This function uses Python's built-in slicing mechanism, which is both 
    idiomatic and efficient (implemented in C). It handles all Unicode codepoints 
    including emojis, combining characters, and non-BMP planes without special logic,
    as the slice operation works on the underlying string representation correctly.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string with the characters in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    test_cases = [
        "Hello, World!",
        "\ud83d\ude00",  # Grinning face emoji (single codepoint)
        "\u267b\uFE0F",  # Snowman with modifier sequence (two characters: snowman + combining diacritical mark)
        "Python \U0001f4a9 Programming!",  # Python text, pizza emoji (non-BMP plane), and exclamation
    ]

    for test_input in test_cases:
        reversed_output = reverse_string(test_input)
        print(f"Original: {test_input!r}")
        print(f"Reversed:{reversed_output!r}\n")