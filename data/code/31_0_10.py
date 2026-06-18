def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    pass
