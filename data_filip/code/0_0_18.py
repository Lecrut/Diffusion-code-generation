def extract_digits_to_int(s):
    digits = ''.join(c for c in s if c.isdigit())
    if not digits:
        return 0
    return int(digits)

if __name__ == '__main__':
    print(extract_digits_to_int("a1b2c3"))
    print(extract_digits_to_int("hello"))
    print(extract_digits_to_int("123"))
    print(extract_digits_to_int("abc"))
    print(extract_digits_to_int("007agent"))
    print(extract_digits_to_int(""))
    print(extract_digits_to_int("x5y6z7"))