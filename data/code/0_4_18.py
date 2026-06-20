def sanitize_to_float(s):
    digits = "".join(c for c in s if c.isdigit())
    if digits:
        return float(digits)
    return float('0')

if __name__ == '__main__':
    result = sanitize_to_float("abc123def45.67ghi")
    print(result)