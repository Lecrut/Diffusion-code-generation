def check_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    return len(set(text_lower)) != len(text_lower)
if __name__ == '__main__':
    sample_strings = [
        "Hello World",                                          
        "Python Programming",                                                              
        "Unique123Chars!",                                                                                   
    ]
    for test_str in sample_strings:
        result = check_repeated_chars(test_str)
        print(f"String: '{test_str}'")
        print(f"Contains repeated characters: {result}")