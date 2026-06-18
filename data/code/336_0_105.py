def contains_repeated_characters(text: str) -> bool:
    normalized_text = text.lower()
    char_count = {}
    for char in normalized_text:
        if char in char_count:
            return True
        else:
            char_count[char] = 1
    return False
def main():
    sample_strings = [
        "Hello World",                                                                                                                                                                                                                     
        "abcdefg",                       
        "The quick brown fox jumps over the lazy dog",                                                                                                                    
        "aaaaa"                                            
    ]
    for test_string in sample_strings:
        result = contains_repeated_characters(test_string)
        status = "Contains repeated characters" if result else "No repeated characters found"
        print(f"'{test_string}': {status}")
if __name__ == '__main__':
    main()