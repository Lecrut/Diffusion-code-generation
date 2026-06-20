import re

_special_char_pattern = re.compile(r'[^\w\s]')

def contains_special_characters(text):
    return bool(_special_char_pattern.search(text))

if __name__ == '__main__':
    print(contains_special_characters("hello world"))
    print(contains_special_characters("hello world!"))
    print(contains_special_characters("test@123"))
    print(contains_special_characters("normal string"))
    print(contains_special_characters("special#$%"))