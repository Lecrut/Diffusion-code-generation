import string

def has_punctuation_or_symbols(s):
    return any(char in string.punctuation for char in s)

if __name__ == '__main__':
    sample_values = [
        "Hello, World!",
        "No punctuation here",
        "12345",
        "Symbols @#$%",
        "",
        "Pure letters only",
        "Mixed: letters, numbers 123, and symbols!"
    ]
    for value in sample_values:
        result = has_punctuation_or_symbols(value)
        print(result)