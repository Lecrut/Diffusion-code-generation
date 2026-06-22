import string

def has_punctuation_or_symbols(text):
    punctuation_set = set(string.punctuation)
    for char in text:
        if char in punctuation_set:
            return True
    return False

if __name__ == '__main__':
    sample_values = [
        "Hello World",
        "Hello, World!",
        "Python3",
        "test@#$",
        "No punctuation here",
        "Has (parentheses)",
        "Special: chars; and, stuff."
    ]
    for sample in sample_values:
        result = has_punctuation_or_symbols(sample)
        print(result)