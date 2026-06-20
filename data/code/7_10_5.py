import re

def has_special_characters(text):
    return bool(re.search(r'[^a-zA-Z0-9]', text))

if __name__ == '__main__':
    test_string_1 = "HelloWorld123"
    test_string_2 = "Hello_World!"
    test_string_3 = "1234567890"
    test_string_4 = "Test@Case#"

    print(has_special_characters(test_string_1))
    print(has_special_characters(test_string_2))
    print(has_special_characters(test_string_3))
    print(has_special_characters(test_string_4))