def check_repeated_chars(text: str) -> bool:
    lower_text = text.lower()
    seen = set()
    for char in lower_text:
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",                                              
        "abcdef",                              
        "Hello World!",                                                                                         
        "aabbcc"                                   
    ]
    for test_str in sample_strings:
        result = check_repeated_chars(test_str)
        print(f"'{test_str}': {'Repeated characters found' if result else 'No repeated characters'}")