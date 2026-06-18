#!/usr/bin/env python3
"""
Script to extract the first letter of each word from a given string.
Handles various whitespace scenarios including multiple spaces, tabs, newlines, 
and leading/trailing whitespaces efficiently using Python's built-in split() method.
"""

def get_first_letters(text: str) -> list[str]:
    """
    Extracts the first character of each non-empty word from the input string.

    Args:
        text (str): The input string containing words separated by whitespace.

    Returns:
        List[str]: A list of single-character strings representing the first letter 
                   of each word found in the input.
    
    Examples:
        >>> get_first_letters("  Hello World! ")
        ['H', 'W']
        >>> get_first_letters("\tPython\nis\tawesome")
        ['P', 'i', 'a']
    """
    if not text or not isinstance(text, str):
        return []

    # The split() method without arguments automatically handles all whitespace 
    # types (spaces, tabs, newlines) and ignores leading/trailing empty strings.
    words = text.split()
    
    result = []
    for word in words:
        if not isinstance(word, str):
            continue
        
        first_char = word[0]
        
        # Ensure the character is a string (it should be by definition of indexing)
        result.append(first_char)

    return result

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, 
    # network access, or pre-existing files are required.
    
    test_cases = [
        "  Hello World! ",           # Leading/trailing spaces and punctuation
        "\tPython\nis\tawesome",     # Tabs and newlines as separators
        "   single word              ", # Multiple internal spaces
        "",                          # Empty string edge case
        "NoSpacesHere123",            # No whitespace at all
    ]

    for test_string in test_cases:
        output = get_first_letters(test_string)
        print(f"Input: {repr(test_string)}")
        print(f"Output: {''.join(output)}")
        print("-" * 40)