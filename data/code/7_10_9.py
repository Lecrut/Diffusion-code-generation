import re

def contains_special_characters(s):
    return bool(re.search(r'[^a-zA-Z0-9]', s))

if __name__ == '__main__':
    print(contains_special_characters("hello"))
    print(contains_special_characters("hello world!"))
    print(contains_special_characters("12345"))
    print(contains_special_characters("test@123"))
    print(contains_special_characters(""))