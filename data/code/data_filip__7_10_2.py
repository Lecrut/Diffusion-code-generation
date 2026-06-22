import re

def contains_special_characters(s):
    return bool(re.search(r'[^a-zA-Z0-9]', s))

if __name__ == '__main__':
    test_string_1 = "HelloWorld123"
    test_string_2 = "Hello@World!"
    test_string_3 = "NoSpecialCharsHere"
    test_string_4 = "Has#Space"

    print(contains_special_characters(test_string_1))
    print(contains_special_characters(test_string_2))
    print(contains_special_characters(test_string_3))
    print(contains_special_characters(test_string_4))