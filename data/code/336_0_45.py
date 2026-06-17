def has_repeated_characters(text: str) -> bool:
    text = text.lower()
    seen_chars = set()
    for char in text:
        if char not in seen_chars:
            seen_chars.add(char)
        else:
            return True
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",                                                       
        "abcdef",                                        
        "Hello World!",                                 
        "",                                                               
        "a"                                                             
    ]
    for test_str in sample_strings:
        result = has_repeated_characters(test_str)
        print(f"'{test_str}' -> {'Repeated characters found' if result else 'No repeated characters'}")