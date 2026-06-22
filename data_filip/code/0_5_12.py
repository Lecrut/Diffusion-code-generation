import unicodedata

def extract_unicode_digits(text):
    result = []
    for char in text:
        if unicodedata.category(char).startswith('Nd'):
            result.append(unicodedata.digit(char))
    return result

if __name__ == '__main__':
    sample_text = "abc123d456\u0967\u0968\u0969"
    print(extract_unicode_digits(sample_text))