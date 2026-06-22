def extract_digits(mixed_string: str) -> str:
    digits = []
    for char in mixed_string:
        if '0' <= char <= '9':
            digits.append(char)
    return ''.join(digits)

if __name__ == '__main__':
    result = extract_digits("abc123xyz456")
    print(result)