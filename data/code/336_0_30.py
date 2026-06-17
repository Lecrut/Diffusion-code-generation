def check_repeated_characters(text: str) -> bool:
    normalized_text = text.lower()
    char_count = {}
    for char in normalized_text:
        char_count[char] = char_count.get(char, 0) + 1
    return len(normalized_text) != len(set(normalized_text))
if __name__ == '__main__':
    sample_strings = [
        "hello",                                          
        "abcdef",                              
        "Hello World!",                                                                                                                                                                                 
    ]
    test_cases = [
        ("hello", True),
        ("abcdef", False),
        ("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz", False),                                       
    ]
    for test_input, expected in test_cases:
        result = check_repeated_characters(test_input)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] Input: '{test_input}' -> Repeated chars: {result}")