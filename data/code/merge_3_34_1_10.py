def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalizes the first letter of every word in the input string,
    leaving all other characters unchanged (including existing casing).

    Args:
        text (str): The input string.

    Returns:
        str: A new string with only the first character of each word capitalized.
    """
    if not isinstance(text, str) or len(text) == 0:
        return ""

    result = []
    
    # Track whether we are at the start of a word to decide capitalization rules
    is_start_of_word = True
    
    for char in text:
        if char.isspace():
            # Reset flag when encountering whitespace (unless it's non-breaking space or similar, but standard spaces suffice here)
            is_start_of_word = True
        elif is_start_of_word and 'a' <= char.lower() <= 'z':
            # Capitalize only the first letter if it's a lowercase alphabetic character.
            # We check specifically for lowercase to avoid double capitalization or changing numbers/symbols at start of word (though typically words start with letters).
            result.append(char.upper())
        else:
            result.append(char)
        
        is_start_of_word = False
    
    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    samples = [
        "hello world",
        "Python Programming Is Fun!",
        "  multiple   spaces ",
        "",
        "no_change_here_123abc",
        "UPPERCASE mixedCase"
    ]

    for sample in samples:
        output = capitalize_first_letter_only(sample)
        print(f'Input: "{sample}" -> Output: "{output}"')