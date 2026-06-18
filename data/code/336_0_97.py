def check_repeated_chars(text: str) -> bool:
    normalized_text = text.lower()
    char_count = {}
    for char in normalized_text:
        if char in char_count:
            return True
        else:
            char_count[char] = 1
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello world",                                   
        "abcdefg",                                       
        "The Quick Brown Fox",                                                                                                
        "aabbccdd"                                             
    ]
    for test_str in sample_strings:
        result = check_repeated_chars(test_str)
        print(f"'{test_str}' has repeated characters: {result}")
    exit(0)