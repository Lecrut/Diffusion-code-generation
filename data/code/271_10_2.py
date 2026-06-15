import string
def classify_string(text):
    alphabetic_count = 0
    numeric_count = 0
    punctuation_count = 0
    whitespace_count = 0
    special_symbol_count = 0
    for char in text:
        if char.isalpha():
            alphabetic_count += 1
        elif char.isdigit():
            numeric_count += 1
        elif char in string.punctuation:
            punctuation_count += 1
        elif char.isspace():
            whitespace_count += 1
        else:
            special_symbol_count += 1
    return {
        "alphabetic": alphabetic_count,
        "numeric": numeric_count,
        "punctuation": punctuation_count,
        "whitespace": whitespace_count,
        "special_symbols": special_symbol_count
    }
if __name__ == '__main__':
    sample_string = "Hello World! 123, this is a test-string."
    result = classify_string(sample_string)
    print(result)