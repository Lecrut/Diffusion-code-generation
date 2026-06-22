def extract_digits_to_string(mixed_string):
    digit_chars = []
    for char in mixed_string:
        ascii_val = ord(char)
        if 48 <= ascii_val <= 57:
            digit_chars.append(char)
    return "".join(digit_chars)

if __name__ == '__main__':
    sample_string = "a1b2c3!@#456"
    result = extract_digits_to_string(sample_string)
    print(result)