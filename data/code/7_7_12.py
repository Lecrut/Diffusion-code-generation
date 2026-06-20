import re

def has_special_chars(s: str) -> bool:
    special_pattern = re.compile(r'[^a-zA-Z0-9]')
    stripped = special_pattern.sub('', s)
    if len(s) != len(stripped):
        return True
    return False

if __name__ == '__main__':
    test_string_1 = "HelloWorld123"
    test_string_2 = "Hello@World!2024"
    result_1 = has_special_chars(test_string_1)
    result_2 = has_special_chars(test_string_2)
    print(result_1)
    print(result_2)