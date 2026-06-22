import string

def has_special_characters(text):
    return any(char in string.punctuation for char in text)

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Hello, World!",
        "Python3.9",
        "NoSpecialChars123",
        "Special@Chars#Here"
    ]
    for s in sample_strings:
        print(f"String: '{s}' -> Has special characters: {has_special_characters(s)}")