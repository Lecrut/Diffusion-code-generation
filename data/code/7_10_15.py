import re

def contains_special_chars(text):
    return bool(re.search(r'[^a-zA-Z0-9]', text))

if __name__ == '__main__':
    sample_string = "Hello World!"
    result = contains_special_chars(sample_string)
    print(result)