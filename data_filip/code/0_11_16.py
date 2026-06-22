def extract_digits_from_string(mixed_string):
    digits = []
    for char in mixed_string:
        ascii_val = ord(char)
        if 48 <= ascii_val <= 57:
            digits.append(char)
    return ''.join(digits)

if __name__ == '__main__':
    sample_mixed_string = "a1b2c3d4e5f6g7h8i9j0"
    result = extract_digits_from_string(sample_mixed_string)
    print(result)