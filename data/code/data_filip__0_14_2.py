def extract_digits_as_ints(s):
    return [int(ch) for ch in s if ch.isdigit()]

if __name__ == '__main__':
    sample = "a1b2c3!@#456xyz789"
    print(extract_digits_as_ints(sample))