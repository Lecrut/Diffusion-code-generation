def capitalize_first_letter(text: str) -> str:
    """
    Capitalizes the first letter of a string, leaving all other letters unchanged.
    
    Handles edge cases such as empty strings and those starting with punctuation 
    by returning exactly one character changed to uppercase if it is alphabetic,
    otherwise returns an empty or original prefix without modification for non-letters.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first letter capitalized if applicable.
    """
    if not text:
        return ""
    
    # Extract just the first character to check and transform only that one
    first_char = text[0]
    
    # Only capitalize if it's an alphabetic character; otherwise leave as is
    if 'a' <= first_char.lower() <= 'z':
        new_first_char = first_char.upper()
        
        return f"{new_first_char}{text[1:]}"
    
    else:
        # If the first char isn't a letter, don't touch it (preserves original behavior)
        return text

if __name__ == '__main__':
    sample_strings = [
        "",                          # Empty string
        "hello",                     # Normal case
        "!Hello!",                   # Starts with punctuation
        "#123abc",                  # Non-letter start followed by letters later
        "aBcDeFgHiJkLmNoPqRsT",    # Single letter input (already handled but explicit)
        "   world",                 # Leading whitespace, first char is space
    ]

    for s in sample_strings:
        result = capitalize_first_letter(s)
        print(f"Input: {s!r} -> Output: {result!r}")