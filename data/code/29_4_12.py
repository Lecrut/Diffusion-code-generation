def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a string, handling Unicode correctly.
    
    This function iterates over the input string and constructs a new reversed 
    string. It properly handles all Unicode characters (e.g., emoji, accented letters),
    as Python strings are sequences of Unicode code points by default.

    Parameters:
        s (str): The input string to be reversed. Can contain any valid Unicode character.

    Returns:
        str: A new string with the characters in reverse order relative to the original.

    Example:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("🚀✨Hello 世界")
        '界世 Hello✨🚀' (Note: Whitespace and emoji positions are also reversed)
    """
    return ''.join(reversed(s))

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    samples = [
        "hello",
        "🚀✨Hello 世界",
        "Python3 is great!",
        "",
        "A" * 100,  # Test with a long string of repeated characters
    ]

    for test_input in samples:
        result = reverse_string(test_input)
        print(f"Input:    '{test_input}'")
        print(f"Output:   '{result}'")
        print("-" * 30)