def has_special_char(text):
    for char in text:
        if not char.isalnum() and not char.isspace():
            return True
    return False

if __name__ == '__main__':
    sample_strings = ["HelloWorld", "Test@123", "NoSpecialCharsHere", "Spaces are ok   ", "Special!@#"]
    for s in sample_strings:
        result = has_special_char(s)
        print(f"Input: '{s}' -> Has Special Char: {result}")