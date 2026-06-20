import string
import re

def count_special_chars_and_check(s: str) -> bool:
    special_count = 0
    special_char_pattern = '[^a-zA-Z0-9\\s]'
    matches = re.findall(special_char_pattern, s)
    special_count = len(matches)
    return special_count > 0
if __name__ == '__main__':
    test_string = 'Hello, World! 123'
    result = count_special_chars_and_check(test_string)
    print(result)
    test_string_2 = 'HelloWorld123'
    result_2 = count_special_chars_and_check(test_string_2)
    print(result_2)