def has_repeated_letters(text: str) -> bool:
    """
    Determines if a given string contains any repeated letters.
    
    Args:
        text (str): The input string to check. Only alphabetic characters are considered; 
                    case-insensitive comparison is used. Other characters (digits, symbols, spaces) 
                    are ignored for the purpose of checking letter repetition.
    
    Returns:
        bool: True if any letter appears more than once in lowercase form, False otherwise.
    """
    seen_letters = set()
    text_lower = text.lower()

    for char in text_lower:
        if 'a' <= char <= 'z':  # Check if character is a letter
            if char in seen_letters:
                return True
            seen_letters.add(char)
    
    return False

if __name__ == '__main__':
    pass
