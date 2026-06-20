def sanitize_to_float(mixed_str):
    digits = ''.join(char for char in mixed_str if char.isdigit())
    if not digits:
        return 0.0
    return float(digits)

if __name__ == '__main__':
    print(sanitize_to_float("abc123.45xyz"))
    print(sanitize_to_float("no-digits-here"))
    print(sanitize_to_float("42"))