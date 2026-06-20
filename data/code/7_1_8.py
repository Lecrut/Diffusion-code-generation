import string

def has_special_characters(text):
    printable_without_punctuation = set(string.printable) - set(string.punctuation) - set(string.whitespace)
    for char in text:
        if char not in printable_without_punctuation:
            return True
    return False

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = has_special_characters(sample_string)
    print(result)