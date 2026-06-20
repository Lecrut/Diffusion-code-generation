def extract_digits(mixed_string):
    result = []
    for char in mixed_string:
        ascii_value = ord(char)
        if 48 <= ascii_value <= 57:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "a1b2c3D4e5f6G7h8i9j0X!@#"
    extracted_digits = extract_digits(sample_input)
    print(extracted_digits)