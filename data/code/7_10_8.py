import re

def contains_special_char(text):
    pattern = r'[^a-zA-Z0-9]'
    return bool(re.search(pattern, text))

if __name__ == '__main__':
    test_string_1 = "HelloWorld123"
    test_string_2 = "Hello@World!"
    test_string_3 = "NoSpecialsHere"
    test_string_4 = "Has a space and a symbol #"
    
    result_1 = contains_special_char(test_string_1)
    result_2 = contains_special_char(test_string_2)
    result_3 = contains_special_char(test_string_3)
    result_4 = contains_special_char(test_string_4)
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)