def extract_digits(s):
    digits = [c for c in s if c.isdigit()]
    if not digits:
        return 0
    return int(''.join(digits))

if __name__ == '__main__':
    print(extract_digits("a1b2c3"))
    print(extract_digits("abc"))
    print(extract_digits("123"))