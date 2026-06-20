import string

def has_special_characters(text):
    special_chars = set(string.punctuation + string.whitespace)
    found = []
    for char in text:
        if ord(char) >= 33 and ord(char) <= 126:
            if char in special_chars:
                found.append(char)
    return found

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    result = has_special_characters(sample_string)
    print(result)