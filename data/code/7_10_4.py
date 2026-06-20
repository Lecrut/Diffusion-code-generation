import re

def contains_special_chars(text: str) -> bool:
    return bool(re.search(r'[^a-zA-Z0-9]', text))

if __name__ == '__main__':
    sample_strings = ["hello_world", "hello world", "Hello123", "hello!@#"]
    for s in sample_strings:
        print(contains_special_chars(s))