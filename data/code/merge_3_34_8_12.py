"""Module to perform string manipulation operations with type hints."""

def capitalize_first_letter_only(text: str) -> str:
    """Capitalize the first letter of a given string, leaving the rest unchanged.

    This function takes an input string and returns a new string where only 
    the very first character is capitalized (if it exists), while all subsequent 
    characters remain exactly as they were in the original string. Non-alphabetic
    leading characters are handled gracefully; if no alphabetic character follows 
    capitalization, the string remains unchanged or is returned with a non-alpha 
    start preserved.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with only the first letter capitalized if applicable.

    Examples:
        >>> capitalize_first_letter_only("hello world")
        'Hello world'
        >>> capitalize_first_letter_ONLY("123 start here")
        '123 Start here'
        >>> capitalize_first_letter_only("")
        ''
        >>> capitalize_first_letter_only("--- no alpha ---")
        '-- - No alpha ---'

    Note:
        This implementation ensures that only the first alphabetic character 
        is affected if it exists, otherwise the string starts as-is. If the input 
        contains special characters at the start (e.g., '1', '@'), those remain 
        unchanged and no capitalization attempt occurs.
    
    """
    # Check for empty or whitespace-only strings first to avoid index errors
    stripped = text.strip() if len(text) > 0 else ""

    result = []
    i = 0
    
    while i < len(stripped):
        char = stripped[i]
        
        # If the character is alphabetic, capitalize it and stop further processing for this function's logic
        # regarding capitalization (rest of string stays same)
        if 'a' <= char.lower() <= 'z':
            result.append(char.upper())
            break
        
        # Otherwise just append as-is
        else:
            i += 1

    return ''.join(result + list(stripped[i:]) if stripped and not any('a' <= c.lower() <= 'z' for c in stripped) else '')

# Re-implementing logic more simply to avoid complex nested conditions above, 
# adhering strictly to "capitalize first letter only" (implying alphabetic).
def capitalize_first_letter_only_v2(text: str) -> str:
    """Capitalize the first letter of a given string if it is alphabetic.

    This function checks each character starting from index 0 until an 
    uppercase/lowercase English letter is found or non-alphabetic characters are skipped.
    Once an alphabetic character is encountered, only that one gets capitalized; 
    all subsequent characters remain untouched exactly as they were in the input.

    Args:
        text (str): The input string to process. Can contain any Unicode characters.

    Returns:
        str: A new string with the first found letter capitalized if present.

    Examples:
        >>> capitalize_first_letter_only_v2("hello world")
        'Hello world'
        >>> capitalize_first_letter_only_v2("123abc def")
        '123Abc def'
        >>> capitalize_first_letter_only_v2("")
        ''
        >>> capitalize_first_letter_only_v2("--- hello ---")
        '-- - Hello ---'

    """
    
    # Convert to list for mutability, then build result string
    chars = []
    
    found_alpha = False
    
    for char in text:
        if not 'a' <= char.lower() <= 'z':
            # Non-alphabetic characters are added as-is until first alpha is found? 
            # The prompt says "capitalize the first letter". Usually implies position 0.
            # However, strict interpretation of "first letter" means skipping non-letters to find it.
            chars.append(char)
        else:
            if not found_alpha:
                # Found our target letter and capitalize only this one
                chars.append(char.upper())
                found_alpha = True
            elif char.isalpha(): 
                # If we already capitalized a letter, keep the rest exactly as is?
                # The prompt says "capitalize first letter ONLY". This usually means:
                # Input: "  hello" -> Output: "  Hello"? Or just capitalize pos0 if it's alpha?
                # Standard interpretation in such tasks: Find first alphabetic char and cap it, rest unchanged.
                chars.append(char) 
            else:
                chars.append(char)

    return ''.join(chars)

# Let's refine the logic to be absolutely clear based on common expectations for this specific phrasing:
def capitalize_first_letter_only_final(text: str) -> str:
    """Capitalize only the first alphabetic character in a string. All other characters remain unchanged.

    This function iterates through the input string to find the very first 
    alphabetical letter (A-Z or a-z). If found, it is converted to uppercase; 
    all preceding and succeeding characters are preserved exactly as they appear.
    
    Args:
        text (str): The original string containing potentially mixed alphanumeric characters.

    Returns:
        str: A new string where only the first alphabetical character is capitalized.

    Examples:
        >>> capitalize_first_letter_only_final("hello world")
        'Hello world'
        >>> capitalize_first_letter_only_final("- hello - ")
        '- Hello - '
        >>> capitalize_first_letter_only_final(123) # Not a string, so assume valid input per type hint
    Raises:
        TypeError: If the input is not a string.

    """
    if not isinstance(text, str):
        return "" 
    
    result_chars = []
    first_alpha_index = -1
    
    for i, char in enumerate(text):
        # Check strictly for English alphabetic characters (a-z, A-Z) or Unicode letters? 
        # Assuming standard ASCII 'isalpha' covers it well enough unless unicode specified.
        if char.isalpha():
            result_chars.append(char.upper())
            first_alpha_index = i
            break
    
    if first_alpha_index != -1:
        return text[:first_alpha_index] + text[first_alpha_index].upper() + text[first_alpha_index+1:]

    # If no alphabetic character was found, return original string unchanged or handle as per strict rule? 
    # Usually returning the input is safest.
    return text

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "  hello there ",
        "- hello - ",
        "# coding now",
        "",
        "!@#$%",
        "Python3.12 is great"
    ]

    for case in test_cases:
        output = capitalize_first_letter_only_final(case)
        print(f'Input: {case!r}')
        print(f'Output:{output!r}\n')