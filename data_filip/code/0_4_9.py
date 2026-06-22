def sanitize_to_float(mixed_string):
    digits_only = ''.join(c for c in mixed_string if c.isdigit())
    if not digits_only:
        return 0.0
    return float(digits_only)

if __name__ == '__main__':
    sample_values = [
        "123abc456",
        "hello314world",
        "12.34.56",
        "abc",
        "007",
        "100%pure",
        "",
        "a1b2c3d4e5",
        "1234567890",
        "-123.45"
    ]
    for val in sample_values:
        result = sanitize_to_float(val)
        print(result)