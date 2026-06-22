def extract_digits_as_integer_string(mixed_string):
    digit_chars = []
    for char in mixed_string:
        ascii_val = ord(char)
        if 48 <= ascii_val <= 57:
            digit_chars.append(char)
    return ''.join(digit_chars)

if __name__ == '__main__':
    sample_input = "a1b2c3d4e5f6g7h8i9j0!@#"
    result = extract_digits_as_integer_string(sample_input)
    print(result)