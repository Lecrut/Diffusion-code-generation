import string
import re

def contains_special_chars(input_string):
    special_chars = set(string.punctuation)
    for char in input_string:
        if char in special_chars:
            return True
    return False

if __name__ == '__main__':
    test_string_1 = "Hello, World!"
    test_string_2 = "NoSpecialCharsHere123"
    test_string_3 = "Mix3d with@Symbols#"
    
    result_1 = contains_special_chars(test_string_1)
    result_2 = contains_special_chars(test_string_2)
    result_3 = contains_special_chars(test_string_3)
    
    print(result_1)
    print(result_2)
    print(result_3)