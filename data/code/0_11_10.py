def extract_digits(input_string):
    digits = []
    for char in input_string:
        if '0' <= char <= '9':
            digits.append(char)
    if not digits:
        return ""
    return "".join(digits)

if __name__ == '__main__':
    mixed_string = "a1b2c3d4e5f6g7h8i9j0"
    result = extract_digits(mixed_string)
    print(result)