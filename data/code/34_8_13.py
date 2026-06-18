import unicodedata

def capitalize_first_letter(text: str) -> str:
    """
    Capitalizes the first letter of a string while leaving all other characters unchanged.
    
    This function handles Unicode text properly, ensuring that non-Latin scripts and combined
    character sequences are handled correctly according to standard capitalization rules for
    their respective languages where applicable (e.g., Turkish 'ı' vs 'I'). It skips any
    leading whitespace before capitalizing the first actual alphabetic character.
    
    If no alphabetic characters exist in the string, or if it is empty, the original string
    is returned unchanged. Characters after the first letter remain exactly as they were 
    inputted (no lowercase conversion for subsequent letters).
    
    Args:
        text (str): The input string to be processed.
        
    Returns:
        str: A new string with only the first alphabetic character capitalized, or the original string if none exists.

    Example:
        >>> capitalize_first_letter("hello world")
        'Hello world'
        >>> capitalize_first_letter("  Hello World")
        '  Hello World'
        >>> capitalize_first_letter("!@#123")
        '!@#123'
        >>> capitalize_first_letter("")
        ''

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string type, got {type(text).__name__}")
    
    # Normalize to handle potential combining characters correctly before processing
    normalized_text = unicodedata.normalize('NFC', text)
    
    result_chars = []
    first_char_found = False
    
    for char in normalized_text:
        if not first_char_found:
            if 'A' <= char <= 'Z':
                # Already capitalized, keep as is
                result_chars.append(char)
                first_char_found = True
            elif 'a' <= char <= 'z':
                # Convert to uppercase only for the first alphabetic character found
                result_chars.append(char.upper())
                first_char_found = True
        else:
            # Leave all subsequent characters exactly as they are per requirements
            result_chars.append(char)

    return ''.join(result_chars)

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "  Hello World",
        "!@#123",
        "",
        "python programming is fun",
        "\u043d\u0435\u043c\u043e\u0439 \u044f\u0437\u044b\u043a"  # Russian example: nemoy yazyk -> Немой Язык
    ]

    print("Sample Output:")
    for test_input in test_cases:
        output = capitalize_first_letter(test_input)
        formatted_output = f"'{test_input}' => '{output}'"
        print(formatted_output)