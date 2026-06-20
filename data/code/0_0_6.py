def extract_digits_to_int(s):
    digits = ''.join(c for c in s if c.isdigit())
    if not digits:
        return 0
    return int(digits)

if __name__ == '__main__':
    print(extract_digits_to_int("a1b2c3"))
    print(extract_digits_to_int("no_digits_here"))
    print(extract_digits_to_int("42is_theway"))
    print(extract_digits_to_int(""))
    print(extract_digits_to_int("007bond"))