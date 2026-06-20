import re

def has_special_characters(s):
    return bool(re.search(r'[^a-zA-Z0-9]', s))

if __name__ == '__main__':
    sample_values = ["hello", "hello123", "hello!", "Hello World", "12345", "", "test@email.com"]
    for value in sample_values:
        print(has_special_characters(value))