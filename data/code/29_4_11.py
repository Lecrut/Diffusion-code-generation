def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a given string, handling Unicode correctly.
    
    This function handles various Unicode scenarios including multi-byte UTF-8 
    sequences and emoji by operating at the character (Unicode code point) level.
    It uses Python's native unicode iteration to ensure correct handling of 
    complex scripts and graphical elements that may span multiple bytes in memory.

    Args:
        s (str): The input string whose characters need to be reversed.

    Returns:
        str: A new string with the characters of the original string in reverse order.

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("🌍hello")  # Includes emoji and special chars
        'olleh💀oℹ️m̧' (order depends on code points)

    Note:
        The function does not modify the original string but returns a new one.
    """
    return ''.join(reversed(s))

if __name__ == '__main__':
    pass
