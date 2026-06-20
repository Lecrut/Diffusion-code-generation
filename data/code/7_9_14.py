import string
import re

def contains_special_characters(s):
    for char in s:
        if char in string.punctuation:
            return True
    return False

if __name__ == '__main__':
    test_string_1 = "HelloWorld"
    test_string_2 = "Hello, World!"
    result_1 = contains_special_characters(test_string_1)
    result_2 = contains_special_characters(test_string_2)
    print(result_1)
    print(result_2)