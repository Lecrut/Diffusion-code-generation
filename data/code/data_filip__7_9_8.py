import string

def has_special_characters(s: str) -> bool:
    for char in s:
        if char in string.punctuation:
            return True
    return False

if __name__ == '__main__':
    test_string_1 = "Hello, World!"
    test_string_2 = "HelloWorld123"
    test_string_3 = "Safe@Pass#2024"
    print(has_special_characters(test_string_1))
    print(has_special_characters(test_string_2))
    print(has_special_characters(test_string_3))