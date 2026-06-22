import re

def contains_special_chars(s: str) -> bool:
    pattern = r'[^a-zA-Z0-9]'
    return bool(re.search(pattern, s))

if __name__ == '__main__':
    test_cases = [
        "Hello123",
        "Hello World!",
        "NoSpecialCharsHere",
        "Special@#Chars",
        "12345",
        "!@#$%",
        ""
    ]
    for text in test_cases:
        result = contains_special_chars(text)
        print(f"Input: '{text}' -> Contains special chars: {result}")