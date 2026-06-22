import re

def contains_special_characters(text):
    return bool(re.search(r'[^a-zA-Z0-9]', text))

if __name__ == '__main__':
    print(contains_special_characters("hello123"))
    print(contains_special_characters("hello@123"))
    print(contains_special_characters(""))
    print(contains_special_characters("aB3"))
    print(contains_special_characters("!@#"))