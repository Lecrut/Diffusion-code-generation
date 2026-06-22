def extract_digits(s):
    return ''.join(c for c in s if c.isdigit())

if __name__ == '__main__':
    sample_inputs = [
        "abc123def456",
        "no digits here",
        "789",
        "a1b2c3",
        "123abc",
        "",
        "x!@#y$%^z&*("
    ]
    for s in sample_inputs:
        result = extract_digits(s)
        print(result)