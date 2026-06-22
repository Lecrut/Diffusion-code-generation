def sanitize_to_float(mixed_string):
    digits_only = ''.join(c for c in mixed_string if c.isdigit())
    if not digits_only:
        return 0.0
    return float(digits_only)

if __name__ == '__main__':
    sample_values = ['123abc', 'abc123', '98.76', 'hello', '007', '12a34b56']
    for s in sample_values:
        result = sanitize_to_float(s)
        print(result)