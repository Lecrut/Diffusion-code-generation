def sanitize_to_float(s):
    digits = [ch for ch in s if ch.isdigit() or ch == '.']
    cleaned = ''.join(digits)
    if not cleaned or cleaned == '.':
        return 0.0
    try:
        return float(cleaned)
    except ValueError:
        return 0.0

if __name__ == '__main__':
    print(sanitize_to_float("abc123.45def"))
    print(sanitize_to_float("100"))
    print(sanitize_to_float("no digits here"))
    print(sanitize_to_float("3.14159"))
    print(sanitize_to_float("12.34.56"))