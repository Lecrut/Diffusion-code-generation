import re

def capitalize_first_only(text: str) -> str:
    """
    Capitalizes the first letter of each word in a multi-word string,
    while ensuring that no other letters within those words are capitalized.
    
    The function handles multiple spaces between words and preserves them.
    It assumes 'word' means any sequence of non-whitespace characters.

    :param text: A string containing one or more words separated by whitespace.
    :return: A new string with the first letter of each word uppercased,
             and all other letters lowercased. Returns an empty string if input is None or only whitespace.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Split into words (sequences of non-whitespace characters) while preserving separators via regex groups
    parts = re.split(r'(\s+)', text.strip())

    processed_parts = []
    
    for part in parts:
        if not part or len(part) == 1 and is_whitespace_only_part(part):
            # If the original string was None, empty, or just whitespace, we return early. 
            # However, since this function handles text passed as a parameter directly via regex splitting above,
            # we handle edge cases where split might produce an extra empty element if there's trailing space after strip.
            processed_parts.append(part)
        elif len(part.strip()) == 1 and part[0] in ' \t\n\r':
             continue
            
        else:
            # Logic for words (sequences of non-whitespace characters):
            first_char = part[0].upper() if part and not is_whitespace_only_part(part) else ''
            rest_chars = [c.lower() for c in part[1:] if len(part) > 1]
            processed_parts.append(first_char + ''.join(rest_chars))

    # Reassemble the string with original whitespace separators. 
    # Since we split by (\s+), every even index is a word, odd indices are separator strings (whitespace).
    
    result = []
    for i in range(0, len(parts) - 1, 2):
        if parts[i].strip(): # It's a word part that was captured
             first_char = parts[i][0] or ''
             rest_chars = [c.lower() for c in parts[i][1:]]
             result.append(first_char.upper() + ''.join(rest_chars))
            
    separator_index = 2

if __name__ == '__main__':
    pass
