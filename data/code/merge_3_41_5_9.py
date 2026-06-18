def case_converter(s):
    """
    Converts a string to lowercase, uppercase, and title-case using 
    manual character manipulation with loops and conditionals.
    
    Args:
        s (str): Input string
        
    Returns:
        dict: A dictionary containing the converted strings for all cases
    """
    result = {
        'lowercase': '',
        'uppercase': '',
        'title_case': ''
    }
    
    # Process each character to create lowercase version
    for char in s:
        if 'a' <= char <= 'z':
            result['lowercase'] += char.lower()
        elif 'A' <= char <= 'Z':
            result['lowercase'] += chr(ord('a') + ord(char) - ord('A'))
        else:
            # Non-alphabetic characters remain unchanged in lowercase conversion
            result['lowercase'] += char
    
    # Process each character to create uppercase version
    for char in s:
        if 'a' <= char <= 'z':
            result['uppercase'] += chr(ord('A') + ord(char) - ord('a'))
        elif 'A' <= char <= 'Z':
            result['uppercase'] += char.upper()
        else:
            # Non-alphabetic characters remain unchanged in uppercase conversion
            result['uppercase'] += char
    
    # Process each character to create title case (first letter of word capitalized)
    prev_space = True  # Assume first character is after a space/start
    for i, char in enumerate(s):
        if 'a' <= char <= 'z':
            if prev_space:
                result['title_case'] += chr(ord('A') + ord(char) - ord('a'))
            else:
                result['title_case'] += char.lower()
        elif 'A' <= char <= 'Z':
            if prev_space:
                result['title_case'] += char.upper()
            else:
                result['title_case'] += chr(ord('a') + ord(char) - ord('A'))
        
        # Check for space or punctuation to determine next character capitalization rule
        if not ('a' <= char <= 'z' and 'A' <= char <= 'Z'):
            prev_space = True
        else:
            prev_space = False
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values - no user input required
    test_strings = [
        "Hello, World!",
        "python is awesome",
        "  Multiple   Spaces ",
        "123 Numbers",
        ""
    ]
    
    print("Case Conversion Results:")
    for original in test_strings:
        converted = case_converter(original)
        print(f"\nOriginal: '{original}'")
        print(f"Lowercase: '{converted['lowercase']}'")
        print(f"Uppercase: '{converted['uppercase']}'")
        print(f"title_case: '{converted['title_case']}'")