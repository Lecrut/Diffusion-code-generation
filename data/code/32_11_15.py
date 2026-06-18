def calculate_phrase_length(phrase: str) -> int:
    """
    Calculate the length of a given string (phrase).

    This function uses Python's built-in len() which is implemented in C,
    making it highly efficient for counting characters. It handles all types
    of strings correctly including Unicode text and empty strings.

    Args:
        phrase (str): The input string whose length needs to be calculated.

    Returns:
        int: The number of characters in the provided string.
    """
    return len(phrase)

if __name__ == '__main__':
    # Sample values - no user input required
    sample_phrases = [
        "",                          # Empty string
        "Hello",                     # Single word
        "Python is awesome!",       # Mixed content
        "1234567890",               # Numeric characters only
        "你好世界",                  # Unicode text (Chinese)
    ]

    for phrase in sample_phrases:
        length = calculate_phrase_length(phrase)
        print(f"Length of '{repr(phrase)}': {length}")