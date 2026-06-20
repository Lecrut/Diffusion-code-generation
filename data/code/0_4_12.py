def sanitize_to_float(s):
    digits_only = ''.join(c for c in s if c.isdigit())
    return float(digits_only) if digits_only else 0.0

if __name__ == '__main__':
    sample1 = "abc123def456"
    sample2 = "789.012xyz"
    sample3 = "no_digits_here"
    print(sanitize_to_float(sample1))
    print(sanitize_to_float(sample2))
    print(sanitize_to_float(sample3))