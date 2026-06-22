def extract_digits_from_mixed_string(input_string):
    digits = []
    for char in input_string:
        if '0' <= char <= '9':
            digits.append(char)
    return "".join(digits)

if __name__ == '__main__':
    mixed_str = "a1b2c3d4e5f6g7h8i9j0"
    result = extract_digits_from_mixed_string(mixed_str)
    print(result)