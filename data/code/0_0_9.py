def extract_digits_to_int(s: str) -> int:
    digits = [ch for ch in s if ch.isdigit()]
    if not digits:
        return 0
    return int(''.join(digits))

if __name__ == '__main__':
    print(extract_digits_to_int("a1b2c3"))
    print(extract_digits_to_int("hello"))
    print(extract_digits_to_int("42 is the answer"))
    print(extract_digits_to_int(""))
    print(extract_digits_to_int("no_digits_here"))
    print(extract_digits_to_int("12345"))