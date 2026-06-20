import string
import re

def has_special_characters(input_string):
    special_chars = set(string.punctuation)
    return any(char in special_chars for char in input_string)

if __name__ == '__main__':
    sample_1 = "HelloWorld"
    sample_2 = "Hello, World!"
    sample_3 = "NoSpecialChars123"
    sample_4 = "Has@Symbol#Here"
    
    print(has_special_characters(sample_1))
    print(has_special_characters(sample_2))
    print(has_special_characters(sample_3))
    print(has_special_characters(sample_4))