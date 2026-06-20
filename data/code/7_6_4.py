import string

def has_special_chars(text):
    allowed = set(string.ascii_letters + string.digits + string.whitespace)
    for char in text:
        if char not in allowed:
            return True
    return False

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "User123",
        "Email@Domain.com",
        "NoSpecialCharsHere",
        "Path/To/File",
        "Tab\tSeparated",
        "Special$ymbol!"
    ]
    for s in sample_strings:
        result = has_special_chars(s)
        print(result)