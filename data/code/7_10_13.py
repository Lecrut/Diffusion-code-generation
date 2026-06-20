import re

def contains_special_characters(s):
    pattern = r'[^a-zA-Z0-9]'
    return bool(re.search(pattern, s))

if __name__ == '__main__':
    test_string_1 = "HelloWorld123"
    test_string_2 = "Hello@World!2024"
    test_string_3 = "NoSpecialCharsHere123"
    test_string_4 = "Has$Symbols#And%Other"
    
    print(contains_special_characters(test_string_1))
    print(contains_special_characters(test_string_2))
    print(contains_special_characters(test_string_3))
    print(contains_special_characters(test_string_4))