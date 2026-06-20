def extract_digits_as_int(s):
    digit_chars = []
    for char in s:
        if 48 <= ord(char) <= 57:
            digit_chars.append(char)
    return "".join(digit_chars)

if __name__ == '__main__':
    sample_string = "Price: $123.45 or 678-90"
    result = extract_digits_as_int(sample_string)
    print(result)