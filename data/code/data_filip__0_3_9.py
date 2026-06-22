def extract_digits(s):
    return ''.join(c for c in s if c.isdigit())

if __name__ == '__main__':
    print(extract_digits("a1b2c3"))
    print(extract_digits("hello world"))
    print(extract_digits("abc123def456"))
    print(extract_digits(""))
    print(extract_digits("12345"))