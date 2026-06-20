import string

def has_punctuation_or_symbols(text):
    return any(char in string.punctuation for char in text)

if __name__ == '__main__':
    sample_values = [
        "Hello World",
        "Hello, World!",
        "No symbols here",
        "12345",
        "Contains @ symbol",
        ""
    ]
    for value in sample_values:
        print(has_punctuation_or_symbols(value))