import string

def has_punctuation_or_symbols(s):
    return any(char in string.punctuation for char in s)

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Hello, World!",
        "No punctuation here",
        "Has symbols: @#$%",
        "Numbers 12345",
        "Mixed: Hello World! @#$%"
    ]
    for s in sample_strings:
        print(has_punctuation_or_symbols(s))