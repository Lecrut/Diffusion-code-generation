def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome, ignoring case and non-alphanumeric characters.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the cleaned string reads the same forwards and backwards, False otherwise.
    
    Example usage:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("No 'x' in Nixon")
        True
    """
    # Filter only alphanumeric characters and convert to lowercase for case-insensitivity check
    cleaned_chars = [c.lower() for c in text if c.isalnum()]

    return "".join(cleaned_chars) == "".join(reversed(cleaned_chars))

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?",
        "Hello, World!",
        "Madam",
        "Python 3.8 is not a palindrome"
    ]

    for test_input in test_cases:
        result = is_palindrome(test_input)
        print(f"'{test_input}' -> {result}")