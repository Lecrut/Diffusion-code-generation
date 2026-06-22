def sanitize_to_float(s):
    digits = [c for c in s if c.isdigit()]
    joined = ''.join(digits)
    if not joined:
        return 0.0
    if '.' in joined:
        parts = joined.split('.')
        integer_part = parts[0]
        fractional_part = parts[1] if len(parts) > 1 else '0'
        float_val = float(f"{integer_part}.{fractional_part}")
    else:
        float_val = float(joined)
    return float_val

if __name__ == '__main__':
    sample_strings = ["123.45", "abc123def456", "789", "!@#noDigits", "3.14159"]
    for s in sample_strings:
        result = sanitize_to_float(s)
        print(result)