def extract_digits_as_string(mixed_string):
    digit_chars = []
    for char in mixed_string:
        ascii_val = ord(char)
        if 48 <= ascii_val <= 57:
            digit_chars.append(char)
    return ''.join(digit_chars)

if __name__ == '__main__':
    sample_strings = [
        "a1b2c3",
        "hello123world",
        "no_digits_here",
        "007jamesbond",
        "99 balloons",
        "",
        "12345",
        "abc123def456ghi789"
    ]
    for s in sample_strings:
        result = extract_digits_as_string(s)
        print(result)