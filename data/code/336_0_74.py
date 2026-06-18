def check_repeated_chars(text):
    text_lower = text.lower()
    seen_characters = set()
    for char in text_lower:
        if char not in seen_characters:
            seen_characters.add(char)
        else:
            return False
    return True
if __name__ == '__main__':
    sample_strings = [
        "hello",                                                                      
        "abcdefg"                                               
    ]
    for test_string in sample_strings:
        result = check_repeated_chars(test_string)
        if result:
            print(f"'{test_string}': Contains NO repeated characters.")
        else:
            print(f"'{test_string}': Contains REPEATED characters.")