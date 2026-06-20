import re

def contains_special_chars(s):
    special_pattern = re.compile(r'[^a-zA-Z0-9\s]')
    return len(s) != len(special_pattern.sub('', s))

if __name__ == '__main__':
    test_string_1 = "Hello World!"
    test_string_2 = "JustPlainLetters123"
    result_1 = contains_special_chars(test_string_1)
    result_2 = contains_special_chars(test_string_2)
    print(result_1)
    print(result_2)