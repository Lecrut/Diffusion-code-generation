def extract_digits(s):
    digits = []
    for char in s:
        if char.isdigit():
            digits.append(int(char))
    return digits

if __name__ == '__main__':
    sample1 = "abc123def456"
    sample2 = "h3ll0 w0rld"
    sample3 = "no digits here"
    sample4 = "0123456789"
    sample5 = "𝟏𝟐𝟑"
    print(extract_digits(sample1))
    print(extract_digits(sample2))
    print(extract_digits(sample3))
    print(extract_digits(sample4))
    print(extract_digits(sample5))