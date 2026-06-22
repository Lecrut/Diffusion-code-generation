def extract_digits_as_int_string(mixed_string):
    digits = []
    for char in mixed_string:
        ascii_val = ord(char)
        if 48 <= ascii_val <= 57:
            digits.append(char)
    return ''.join(digits)

if __name__ == '__main__':
    sample = "a1b2c3!@#45d6"
    result = extract_digits_as_int_string(sample)
    print(result)