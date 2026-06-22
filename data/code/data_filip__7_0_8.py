import re

SPECIAL_CHAR_PATTERN = re.compile(r'[^a-zA-Z0-9\s]')

def contains_special_chars(text):
    return bool(SPECIAL_CHAR_PATTERN.search(text))

if __name__ == '__main__':
    sample_1 = "HelloWorld"
    sample_2 = "Hello_World!"
    sample_3 = "Password@123"
    sample_4 = "Plain text without symbols"
    sample_5 = "12345"
    
    result_1 = contains_special_chars(sample_1)
    result_2 = contains_special_chars(sample_2)
    result_3 = contains_special_chars(sample_3)
    result_4 = contains_special_chars(sample_4)
    result_5 = contains_special_chars(sample_5)
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)