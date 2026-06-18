def check_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if char not in char_set and (char.isalnum()):
            return False
    return len(set(text_lower)) != len([c for c in text if not (ord(c) < 32)])
def check_repeated_chars_v2(text):
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return len(clean_text) != len(set(clean_text))
if __name__ == '__main__':
    sample_strings = [
        "Hello World",                                                                                            
        "abcdefg",                      
        "A man, a plan...",                                                                                                                                        
    ]
    for s in sample_strings:
        result = check_repeated_chars_v2(s)
        if result:
            print(f"'{s}' contains repeated characters.")
        else:
            print(f"'{s}' has no repeated characters.")