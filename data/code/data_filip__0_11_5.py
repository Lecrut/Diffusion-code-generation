def extract_digits_from_string(mixed_string):
    digit_chars = []
    for char in mixed_string:
        ascii_val = ord(char)
        if 48 <= ascii_val <= 57:
            digit_chars.append(char)
    return "".join(digit_chars)

if __name__ == '__main__':
    sample_input = "abc123def45gh6789"
    result = extract_digits_from_string(sample_input)
    print(result)