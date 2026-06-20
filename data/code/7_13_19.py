def has_special_characters(text):
    for char in text:
        if not (char.isalnum() or char.isspace()):
            return True
    return False

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Hello World!",
        "Python3.9",
        "NoSpecialChars123",
        "Has@Symbol",
        "   spaces only   ",
        "Mix of 123 and ABC!",
        "ValidString_WithUnderscore"
    ]
    for s in sample_strings:
        print(has_special_characters(s))