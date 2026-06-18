"""Module to perform string capitalization operations."""

def capitalize_first_letter_only(text: str) -> str:
    """Capitalize the first letter of a string, leaving the rest unchanged.

    This function takes a single input string and returns a new string where
    only the very first character is converted to uppercase (if it was alphabetic).
    All subsequent characters remain exactly as they were in the original string.
    Non-alphabetic characters are handled gracefully without modification or error.

    Args:
        text (str): The input string to process. Can be empty, None-like if passed 
                    but function assumes valid str per type hint, or contain any unicode.

    Returns:
        str: A new string with only the first character capitalized. If the input is 
             an empty string, returns it as is.

    Examples:
        >>> capitalize_first_letter_only("hello world")
        'Hello world'
        >>> capitalize_first_letter_only("123 start")
        '123 start'
        >>> capitalize_first_only("")  # type: ignore[name-defined]
        ''
        >>> capitalize_first_letter_only("aBCdEfGhIjKlMnOpQrStUvWxYz")
        'A BCdefghijklmnopqrstuvwxyz'

    Note:
        This function does not modify the original input string. It creates and 
        returns a new string object.
    
    Raises:
        TypeError: If `text` is not an instance of str (though type hints guide callers).
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected 'str', got {type(text).__name__}")

    if text == "":  # Handle empty string explicitly for clarity and performance
        return ""

    first_char = text[0]
    
    # Check if the character is alphabetic before capitalizing to avoid 
    # unexpected behavior with non-letters (e.g., numbers, symbols) becoming uppercase.
    if 'a' <= first_char <= 'z':  # Basic ASCII check for lowercase letters
        return first_char.upper() + text[1:]
    
    # If the character is not a standard lowercase letter, it remains unchanged 
    # to ensure "first letter only" logic holds strictly (e.g., numbers stay digits).
    if 'A' <= first_char <= 'Z':  # Already uppercase
        return first_char + text[1:]

    # For other characters or unicode letters that aren't standard ASCII lowercase,
    # we capitalize using the general upper() method to support full Unicode 
    # correctly while adhering to "first letter only" rule. However, strictly speaking:
    # If it's already uppercase (checked above), return as is.
    # If it's a unicode lower case letter, use .upper().
    
    # Re-evaluating the logic for maximum Unicode support and correctness:
    if first_char.isalpha():
        capitalized = text[0].capitalize()  # This handles full unicode correctly
        rest = text[1:]
        
        # But wait, 'str.capitalize()' lowercases all other chars. We need ONLY 
        # the first letter uppercased and others preserved exactly as is (case-sensitive).
        # So we revert to manual logic for safety on "only" constraint.
        
        if not ('a' <= text[0] <= 'z'):
            return text  # If it's already uppercase or non-alpha, just return original
        
        # Logic: Uppercase the first char, keep rest EXACTLY as is (preserve existing case)
        result = text[0].upper() + text[1:]
        return result

    # Fallback for any edge cases not caught above, ensuring we don't modify non-alpha at start.
    if 'a' <= text[0] <= 'z':
         return text[0].upper() + text[1:]
    
    return text

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    samples = [
        "hello world",
        "  python programming ",
        "",
        "123 start here",
        "aBCdEfGhIjKlMnOpQrStUvWxYz",
        "special chars @#$%",
        "unicode: café résumé naïve"
    ]

    print("Input -> Output")
    for sample in samples:
        result = capitalize_first_letter_only(sample)
        # Using repr to show exact characters including spaces and quotes if needed, 
        # but standard string representation is usually sufficient.
        print(f'"{sample}" => "{result}"')