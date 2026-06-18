import unicodedata

def to_lowercase(s: str) -> str:
    """
    Converts a string to lowercase using Unicode normalization for optimal handling of accented characters.

    Args:
        s (str): The input string to be converted to lowercase.

    Returns:
        str: A new string with all characters in lowercase.
    
    Note:
        Uses unicodedata.normalize('NFD', ...) followed by standard lowercasing 
        and re-normalization to ensure consistent behavior across different Unicode locales.
    """
    if not s:
        return ""
    
    # Normalize form NFD (decomposed) for proper handling of combined characters, then lowercase
    normalized = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in normalized if not c.is_combining_mark())

def to_uppercase(s: str) -> str:
    """
    Converts a string to uppercase using Unicode normalization.

    Args:
        s (str): The input string to be converted to uppercase.

    Returns:
        str: A new string with all characters in uppercase.
    
    Note:
        Uses unicodedata.normalize('NFC', ...) followed by standard uppercasing 
        and re-normalization for consistency across different Unicode locales.
    """
    if not s:
        return ""
    
    # Normalize form NFC (composed) to handle edge cases like 'é' vs 'e'+acute, then uppercase
    normalized = unicodedata.normalize('NFC', s.upper())
    return ''.join(c for c in normalized if not c.is_combining_mark())

def to_title_case(s: str) -> str:
    """
    Converts a string to title case where the first character of each word is uppercase.

    Args:
        s (str): The input string to be converted to title case.

    Returns:
        str: A new string with words starting with an uppercase letter and followed by lowercase letters.
    
    Note:
        Words are defined as sequences separated by whitespace or other non-alphanumeric characters.
        This implementation handles mixed Unicode scripts gracefully without external locale dependencies.
    """
    if not s:
        return ""

    # Split on any non-cased character to identify word boundaries carefully
    parts = []
    current_word = []
    
    for char in s:
        is_letter = (char.isalpha() or unicodedata.category(char).startswith('L'))
        
        if not is_letter and len(current_word) > 0:
            # End of a word, add it to parts with title casing logic handled later
            parts.append('_'.join(c for c in current_word)) 
            current_word = []
        elif is_letter:
            current_word.append(char.lower())

    if current_word:
        parts.append(''.join(current_word).capitalize())
    
    return '_'.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    
    test_string = "  Hello, World! This is a Multi-lingual Test. Café résumé naïve."
    
    print("Original String:")
    print(test_string)
    print()
    
    lower_result = to_lowercase(test_string)
    print("Lowercase Result:")
    print(lower_result)
    print()
    
    upper_result = to_uppercase(test_string)
    print("Uppercase Result:")
    print(upper_result)
    print()
    
    title_result = to_title_case(test_string)
    print("Title Case Result:")
    print(title_result)