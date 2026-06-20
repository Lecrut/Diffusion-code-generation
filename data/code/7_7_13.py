import re

def contains_special_characters(s: str) -> bool:
    special_pattern = r'[^a-zA-Z0-9\s]'
    stripped_length = len(re.sub(special_pattern, '', s))
    original_length = len(s)
    return original_length != stripped_length

if __name__ == '__main__':
    test_string_1 = "HelloWorld"
    test_string_2 = "Hello@World"
    result_1 = contains_special_characters(test_string_1)
    result_2 = contains_special_characters(test_string_2)
    print(result_1)
    print(result_2)