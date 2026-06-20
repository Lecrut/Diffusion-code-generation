def extract_digits(s):
    return ''.join(c for c in s if c.isdigit())

if __name__ == '__main__':
    sample = "a1b2c3d4e5"
    print(extract_digits(sample))
    sample2 = "no digits here"
    print(extract_digits(sample2))
    sample3 = "007-2000"
    print(extract_digits(sample3))