def extract_digits(text):
    result = []
    for char in text:
        if char.isdigit():
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "a1b2c3d4e5"
    digits = extract_digits(sample_text)
    print(digits)