import sys
def check_repeated_chars(text: str) -> bool:
    normalized_text = text.lower()
    char_count = {}
    for char in normalized_text:
        if not char.isalnum():                                                                                                                                                                                                                                                                                                                                                                                                                     
            pass
        char_count[char] = char_count.get(char, 0) + 1
    for count in char_count.values():
        if count > 1:
            return True
    return False
def main():
    test_strings = [
        "hello",                                                                                                                                                            
        "abcdef",                           
        "A man a plan...",                                                                                                             
        "no-repeat-here",                   
        "python is fun"                                                                                
    ]
    for test_str in test_strings:
        result = check_repeated_chars(test_str)
        if result:
            print(f"'{test_str}' contains repeated characters.")
        else:
            print(f"'{test_str}' has no repeated characters.")
if __name__ == '__main__':
    main()