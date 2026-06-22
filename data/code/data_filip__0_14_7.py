def extract_digits(s):
    return [int(ch) for ch in s if ch.isdigit()]

if __name__ == '__main__':
    sample = "a1b2c3!@#4d5"
    print(extract_digits(sample))