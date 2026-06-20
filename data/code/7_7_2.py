import re

def contains_special_characters(s):
    if s is None:
        return False
    special_pattern = re.compile(r'[^a-zA-Z0-9\s]')
    length_original = len(s)
    length_stripped = len(special_pattern.sub('', s))
    return length_original != length_stripped

if __name__ == '__main__':
    test_string_1 = "Hello World"
    test_string_2 = "Hello! World?"
    test_string_3 = "NoSpecialChars123"
    test_string_4 = "@#$%^&*()"
    
    result_1 = contains_special_characters(test_string_1)
    result_2 = contains_special_characters(test_string_2)
    result_3 = contains_special_characters(test_string_3)
    result_4 = contains_special_characters(test_string_4)
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)