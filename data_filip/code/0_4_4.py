def sanitize_and_convert_to_float(s):
    digits = [c for c in s if c.isdigit()]
    if not digits:
        raise ValueError("No digits found in string")
    return float(''.join(digits))

if __name__ == '__main__':
    sample_values = ["12.34abc", "5678", "a1b2c3", "no_digits_here", "99.99"]
    for val in sample_values:
        try:
            result = sanitize_and_convert_to_float(val)
            print(result)
        except ValueError as e:
            print(e)