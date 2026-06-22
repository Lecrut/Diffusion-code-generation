def sanitize_to_float(mixed_string):
    digits_only = ''.join(ch for ch in mixed_string if ch.isdigit() or ch == '.' or ch == '-')
    if not digits_only:
        return 0.0
    return float(digits_only)

if __name__ == '__main__':
    print(sanitize_to_float("abc123.45xyz"))
    print(sanitize_to_float("price: -99.9"))
    print(sanitize_to_float("no numbers here"))
    print(sanitize_to_float("42"))
    print(sanitize_to_float("3.14159"))