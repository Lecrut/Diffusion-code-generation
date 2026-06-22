def extract_digits_as_int(s):
    digits = ''.join(c for c in s if c.isdigit())
    if not digits:
        return 0
    return int(digits)

if __name__ == '__main__':
    samples = [
        'a1b2c3',
        '123',
        'abc',
        '',
        'x42y7z',
        'no_digits_here!',
        '007'
    ]
    for sample in samples:
        print(extract_digits_as_int(sample))