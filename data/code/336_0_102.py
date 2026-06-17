def check_repeated_chars(text):
    text_lower = text.lower()
    char_count = {}
    for char in text_lower:
        if not char.isalnum():                                                                                                                                                                                                                                     
            pass
        if char in char_count:
            return True
        else:
            char_count[char] = 1
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",                                                      
        "abcdefg",                                      
        "Hello World!",                                                                                                                                                                
    ]
    for s in sample_strings:
        result = check_repeated_chars(s)
        print(f"String '{s}': {'Contains repeated characters' if result else 'No repeated characters'}")