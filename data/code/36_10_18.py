def reverse_string(text: str) -> str:
    """
    Returns a new string with characters in 'text' reversed.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: A new string containing the characters of 'text' in reverse order.

    Example:
        >>> reverse_string("hello")
        "olleh"
    """
    return text[::-1]

if __name__ == '__main__':
    sample_input = "Hello, World!"
    
    result = reverse_string(sample_input)
    print(result)