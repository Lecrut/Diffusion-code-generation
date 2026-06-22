def extract_digits(s):
    return [int(c) for c in s if c.isdigit()]

if __name__ == '__main__':
    print(extract_digits("a1b2c3d4"))