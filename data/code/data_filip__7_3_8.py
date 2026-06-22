import re

def has_special_characters(text):
    return bool(re.search(r'[^a-zA-Z0-9\s]', text))

if __name__ == '__main__':
    print(has_special_characters("Hello, World!"))
    print(has_special_characters("Hello World"))