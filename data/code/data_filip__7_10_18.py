import re

def contains_special_characters(text):
    pattern = re.compile(r'[^a-zA-Z0-9]')
    return bool(pattern.search(text))

if __name__ == '__main__':
    sample_string_1 = "HelloWorld123"
    sample_string_2 = "Hello@World!2023"
    sample_string_3 = "NoSpecialCharsHere"
    sample_string_4 = "C++_is_fun"
    
    print(contains_special_characters(sample_string_1))
    print(contains_special_characters(sample_string_2))
    print(contains_special_characters(sample_string_3))
    print(contains_special_characters(sample_string_4))