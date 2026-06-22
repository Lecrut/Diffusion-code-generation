import re

_SPECIAL_CHAR_PATTERN = re.compile(r"[^a-zA-Z0-9\s]")

def contains_special_chars(s: str) -> bool:
    return bool(_SPECIAL_CHAR_PATTERN.search(s))

if __name__ == '__main__':
    test_string_1 = "HelloWorld"
    test_string_2 = "Hello@World"
    test_string_3 = "12345"
    test_string_4 = "Test#String!"

    result_1 = contains_special_chars(test_string_1)
    result_2 = contains_special_chars(test_string_2)
    result_3 = contains_special_chars(test_string_3)
    result_4 = contains_special_chars(test_string_4)

    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)