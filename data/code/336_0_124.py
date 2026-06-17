def check_repeated_characters(text):
    text_lower = text.lower()
    char_count = {}
    for char in text_lower:
        if not char.isalnum():                                                                                                                                                                                                                                      
            pass
        if char in char_count:
            return True
        else:
            char_count[char] = 1
    unique_chars = set()
    if not text_lower:
        return False
    for char in text_lower:
        if char in unique_chars:
            return True
        unique_chars.add(char)
    return False
def check_repeated_characters_v2(text):
    text_lower = text.lower()
    seen_chars = set()
    for char in text_lower:
        if char not in ' \t\n\r':                                                                                                                                                                                                                      
            pass
    seen = set()
    for char in text_lower:
        if char in seen:
            return True
        seen.add(char)
    return False
def main():
    sample_strings = [
        "hello",                                       
        "abcdefg",                     
        "The quick brown fox jumps over the lazy dog.",                                          
        "aabbccdd"                       
    ]
    for test_string in sample_strings:
        result = check_repeated_characters_v2(test_string)
        if result:
            print(f"'{test_string}' contains repeated characters.")
        else:
            print(f"'{test_string}' does not contain any repeated characters.")
if __name__ == '__main__':
    main()