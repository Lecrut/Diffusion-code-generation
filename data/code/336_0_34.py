def has_repeated_characters(s: str) -> bool:
    s_lower = s.lower()
    seen_chars = set()
    for char in s_lower:
        if char in seen_chars:
            return True
        seen_chars.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",                                                      
        "abcdefg",                                       
        "Hello World!",                                                                                                                                                    
    ]
    for test_str in sample_strings:
        result = has_repeated_characters(test_str)
        print(f"String '{test_str}': {'Has repeated characters' if result else 'No repeated characters'}")