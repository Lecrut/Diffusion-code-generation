import unicodedata

def extract_digits(mixed_string):
    digits = []
    for char in mixed_string:
        if unicodedata.category(char).startswith('Nd'):
            digits.append(int(char))
    return digits

if __name__ == '__main__':
    sample_text = "Hello 123 World ٤٥٦"
    result = extract_digits(sample_text)
    print(result)