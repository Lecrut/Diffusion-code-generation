def extract_digits_preserve_order(s: str) -> list:
    return [char for char in s if char.isdigit()]
if __name__ == '__main__':
    samples = ['a1b2c3', 'hello45world', 'no_digits_here', '12345', 'abc!@#$%', '7x8y9z', '', '0.123.456', 'a1b@c2d#e3f']
    for sample in samples:
        result = extract_digits_preserve_order(sample)
        print(f'Input: {sample!r} -> Digits: {result}')