def extract_digits_from_string(mixed_string):
    result = ""
    for char in mixed_string:
        ascii_val = ord(char)
        if 48 <= ascii_val <= 57:
            result += char
    return result

if __name__ == '__main__':
    sample_input = "a1b2c3!@#456xyz789"
    extracted = extract_digits_from_string(sample_input)
    print(extracted)