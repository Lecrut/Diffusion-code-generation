import string

def has_special_characters(s: str) -> bool:
    special_chars = string.punctuation
    return any(char in special_chars for char in s)

if __name__ == '__main__':
    test_strings = [
        "Hello World",
        "Hello, World!",
        "NoSpecialChars123",
        "Has@Special#Char$"
    ]
    for s in test_strings:
        result = has_special_characters(s)
        print(result)