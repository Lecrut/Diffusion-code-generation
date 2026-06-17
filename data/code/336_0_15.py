def has_repeated_characters(text: str) -> bool:
    text_lower = text.lower()
    char_count = {}
    for char in text_lower:
        if char not in char_count:
            char_count[char] = 0
        else:
            return True
    return False
def main():
    sample_strings = [
        "Hello World",                                                                    
        "abcdefg",                               
        "AaBbCcDdEeFfGgHhIiJjKkLlmnnooppqrrssttuuvvwwxxyyzzz",                        
    ]
    for test_string in sample_strings:
        result = has_repeated_characters(test_string)
        print(f"String: '{test_string}'")
        if result:
            print("Result: Contains repeated characters.")
        else:
            print("Result: No repeated characters found.")
if __name__ == '__main__':
    main()