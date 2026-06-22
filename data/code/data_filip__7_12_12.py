import string

def has_punctuation_or_symbols(text):
    if not isinstance(text, str):
        return False
    for char in text:
        if char in string.punctuation:
            return True
    return False

if __name__ == '__main__':
    samples = [
        "Hello world",
        "Hello, world!",
        "No punctuation here",
        "Has symbols @#$",
        "",
        "12345",
        "Mixed: text and punctuation!"
    ]
    for sample in samples:
        result = has_punctuation_or_symbols(sample)
        print(result)