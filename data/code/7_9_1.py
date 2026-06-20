import string
import re

def has_special_characters(s):
    for char in s:
        if char in string.punctuation:
            return True
    return False

if __name__ == '__main__':
    test_string_1 = "HelloWorld123"
    test_string_2 = "Hello, World!"
    test_string_3 = "NoSpecialChars123"
    test_string_4 = "Use@Symbol#Here"
    
    print(has_special_characters(test_string_1))
    print(has_special_characters(test_string_2))
    print(has_special_characters(test_string_3))
    print(has_special_characters(test_string_4))