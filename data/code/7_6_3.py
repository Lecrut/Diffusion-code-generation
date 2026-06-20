import re

def has_special_chars_excluding_whitespace(text):
    pattern = re.compile(r'[\W_]')
    match = pattern.search(text)
    if match is None:
        return False
    char = match.group()
    if char.isspace():
        return False
    return True

if __name__ == '__main__':
    result1 = has_special_chars_excluding_whitespace("hello world")
    print(result1)
    result2 = has_special_chars_excluding_whitespace("hello! world")
    print(result2)
    result3 = has_special_chars_excluding_whitespace("hello_world")
    print(result3)
    result4 = has_special_chars_excluding_whitespace("hello\tworld")
    print(result4)
    result5 = has_special_chars_excluding_whitespace("hello\nworld")
    print(result5)
    result6 = has_special_chars_excluding_whitespace("@#$%")
    print(result6)