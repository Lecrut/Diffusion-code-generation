def extract_digits_from_string(input_string):
    digits = []
    for char in input_string:
        if '0' <= char <= '9':
            digits.append(char)
    return ''.join(digits)

if __name__ == '__main__':
    mixed_string = "abc123def456ghi789"
    result = extract_digits_from_string(mixed_string)
    print(result)