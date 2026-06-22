def extract_digits(s):
    return ''.join(c for c in s if c.isdigit())

if __name__ == '__main__':
    sample1 = "abc123def456"
    sample2 = "no digits here"
    sample3 = "9a8b7c6d5e4f3g2h1"
    print(extract_digits(sample1))
    print(extract_digits(sample2))
    print(extract_digits(sample3))