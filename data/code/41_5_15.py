def case_converter(s):
    """
    Converts a string to lowercase, uppercase, and title-case manually 
    using loops and conditional logic without built-in string methods like .lower(), .upper(), or .title().
    
    Args:
        s (str): The input string.
        
    Returns:
        dict: A dictionary containing the lowercased, uppercased, and titled versions of the string.
    """
    result = {
        'lowercase': '',
        'uppercase': '',
        'title_case': ''
    }

    # Helper function to check if a character is alphabetic (a-z or A-Z)
    def is_alpha(char):
        return ('a' <= char <= 'z') or ('A' <= char <= 'Z')

    for i in range(len(s)):
        char = s[i]
        
        # Lowercase conversion: if alpha and uppercase, convert to lowercase; otherwise keep as is.
        if is_alpha(char) and 'a' < char <= 'z':
            result['lowercase'] += chr(ord(char) + 32)
        else:
            result['lowercase'] += char

        # Uppercase conversion: if alpha and lowercase, convert to uppercase; otherwise keep as is.
        if is_alpha(char) and 'A' > char >= 'a':
            result['uppercase'] += chr(ord(char) - 32)
        else:
            result['uppercase'] += char

    # Title case conversion: First character of the string to uppercase, rest lowercase (simplified logic for spaces).
    if len(s) == 0:
        result['title_case'] = ''
    elif is_alpha(s[0]):
        first_char_lower_code = ord(s[0]) + 32 if 'a' < s[0] <= 'z' else s[0]
        rest_str = ""
        
        for i in range(1, len(s)):
            char = s[i]
            # If current char is alpha and uppercase, make it lowercase; 
            # otherwise keep as is (including spaces).
            if is_alpha(char) and 'a' < char <= 'z':
                rest_str += chr(ord(char) + 32)
            else:
                rest_str += char
        
        result['title_case'] = first_char_lower_code + rest_str

    return result

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies.
    samples = [
        "Hello World",
        "python programming",
        "",
        "123 ABC xyz"
    ]

    for s in samples:
        output = case_converter(s)
        print(f"Input: '{s}'")
        print(f"Lowercase: {output['lowercase']}")
        print(f"Uppercase: {output['uppercase']}")
        print(f"Title Case: {output['title_case']}")
        print("-" * 20)