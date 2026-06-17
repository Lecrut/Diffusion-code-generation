import sys
def has_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    seen = set()
    for char in text_lower:
        if char not in seen and char.isalpha():                                                                                                                                                                                                                                                                                                                                   
            seen.add(char)
    return len(seen) != len(text_lower)
def main():
    sample_strings = [
        "Hello World",                                                                                                                                      
        "abcdefg",                  
        "aabbccdd",                             
        "Python3",                                                                                                                                                                                                         
    ]
    for test_str in sample_strings:
        result = has_repeated_chars(test_str)
        if result:
            print(f"'{test_str}' contains repeated characters.")
        else:
            print(f"'{test_str}' has no repeated characters.")
if __name__ == '__main__':
    main()