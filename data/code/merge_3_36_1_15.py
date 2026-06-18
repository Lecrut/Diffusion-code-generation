def reverse_string(text: str) -> str:
    """
    Returns a new string with characters in reversed order using slicing notation.

    Args:
        text (str): The input string to be reversed.

    Returns:
        str: A newly allocated string containing the reversed sequence of characters.
    
    Example:
        >>> reverse_string("hello")
        "olleh"
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = ["Hello, World!", "", "a", "Python is awesome."]

    for original in samples:
        reversed_str = reverse_string(original)
        print(f"Original: '{original}'")
        print(f"Reversed: '{reversed_str}'\n")