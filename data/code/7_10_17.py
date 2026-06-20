import re

def has_special_chars(text):
    pattern = r'[^a-zA-Z0-9]'
    return bool(re.search(pattern, text))

if __name__ == '__main__':
    print(has_special_chars("Hello, World!"))
    print(has_special_chars("HelloWorld123"))