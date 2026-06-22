def extract_digits_as_integer_string(mixed_string):
    digits = []
    for char in mixed_string:
        ascii_value = ord(char)
        if 48 <= ascii_value <= 57:
            digits.append(char)
    return ''.join(digits)

if __name__ == '__main__':
    sample_input = "abc123def456ghi789"
    result = extract_digits_as_integer_string(sample_input)
    print(result)