import string
import re

def contains_special_characters(text: str) -> bool:
    special_chars = set(string.punctuation)
    stripped_chars = set(text) - special_chars
    stripped_text_len = len(stripped_chars)
    original_len = len(set(text))
    return original_len != stripped_text_len

if __name__ == '__main__':
    result1 = contains_special_characters("Hello, World!")
    print(result1)
    
    result2 = contains_special_characters("HelloWorld")
    print(result2)
    
    result3 = contains_special_characters("12345")
    print(result3)