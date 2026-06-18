def has_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    return len(set(text_lower)) != len(text_lower)
if __name__ == '__main__':
    sample_strings = [
        "Hello",                                     
        "Python",                                    
        "aabbcc",                      
        "abcdefg",                      
        "The Quick Brown Fox"                   
    ]
    for test_str in sample_strings:
        result = has_repeated_chars(test_str)
        print(f"'{test_str}': {'Repeated characters found' if result else 'No repeated characters'}")