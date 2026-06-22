def extract_digits(input_string: str) -> str:
    digits = []
    for char in input_string:
        ascii_val = ord(char)
        if 48 <= ascii_val <= 57:
            digits.append(char)
    return ''.join(digits)

if __name__ == '__main__':
    mixed_string = "abc123!@#456def789"
    result = extract_digits(mixed_string)
    print(result)