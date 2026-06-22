import string
import re

def contains_special_chars(s):
    return any(char in string.punctuation for char in s)

if __name__ == '__main__':
    test_string_1 = "Hello World"
    test_string_2 = "Hello@World!"
    print(contains_special_chars(test_string_1))
    print(contains_special_chars(test_string_2))