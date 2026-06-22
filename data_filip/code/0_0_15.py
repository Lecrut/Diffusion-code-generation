def extract_digits_as_integer(s):
    digits = [c for c in s if c.isdigit()]
    if not digits:
        return 0
    return int(''.join(digits))

if __name__ == '__main__':
    print(extract_digits_as_integer("abc123def456"))
    print(extract_digits_as_integer("no_digits_here"))
    print(extract_digits_as_integer("99bottles"))
    print(extract_digits_as_integer(""))
    print(extract_digits_as_integer("a1b2c3"))