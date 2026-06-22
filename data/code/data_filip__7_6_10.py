import string

def has_special_characters(text):
    alnum = set(string.ascii_letters + string.digits)
    for char in text:
        if char not in alnum and not char.isspace():
            return True
    return False

if __name__ == '__main__':
    samples = [
        "Hello World",
        "Hello, World!",
        "12345",
        "Test@123",
        "NoSpecialCharsHere",
        "   ",
        "Special#Char"
    ]
    for sample in samples:
        result = has_special_characters(sample)
        print(f"'{sample}': {result}")