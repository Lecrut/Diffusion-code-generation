import string

def has_special_characters(text):
    special_chars = set("!@#$%^&*()-_=+[]{}|;:',.<>?/`~")
    return any(char in special_chars for char in text)

if __name__ == '__main__':
    test_strings = [
        "Hello World",
        "Hello@World",
        "NoSpecialChars123",
        "Has#Special!",
        "JustLetters"
    ]
    results = [has_special_characters(s) for s in test_strings]
    for s, res in zip(test_strings, results):
        print(f"{res}")