def extract_digits(s):
    return [int(c) for c in s if c.isdigit()]

if __name__ == '__main__':
    sample = "a1b2c3!@#45d6"
    print(extract_digits(sample))