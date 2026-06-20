def extract_digits(text):
    digits = []
    for char in text:
        code = ord(char)
        if 48 <= code <= 57:
            digits.append(char)
    return ''.join(digits)

if __name__ == '__main__':
    sample_string = "abc123def456ghi789jkl"
    result = extract_digits(sample_string)
    print(result)