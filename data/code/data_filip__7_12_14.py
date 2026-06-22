import string

def has_punctuation_or_symbols(text):
    punctuation_symbols = set(string.punctuation)
    for char in text:
        if char in punctuation_symbols:
            return True
    return False

if __name__ == '__main__':
    sample_values = [
        "Hello, world!",
        "No punctuation here",
        "Special @#$ symbols",
        "Just numbers 12345",
        "Mixed content: Hello & goodbye!"
    ]
    for value in sample_values:
        result = has_punctuation_or_symbols(value)
        print(result)