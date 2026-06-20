import string
import re

def contains_special_characters(input_string):
    pattern = re.compile(f"[{re.escape(string.punctuation)}]")
    return bool(pattern.search(input_string))

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "Hello, World!",
        "Password123",
        "No special chars here",
        "C@n Y0u F1nd Sp3c!@l Ch@r5?",
        "123456",
        "!@#$%^&*()"
    ]
    for test in test_cases:
        print(contains_special_characters(test))