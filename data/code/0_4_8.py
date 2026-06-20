def sanitize_string(s: str) -> float:
    digits = ''.join(c for c in s if c.isdigit())
    if not digits:
        return 0.0
    return float(digits)

if __name__ == '__main__':
    sample_string = "abc123.45def!@#678"
    result = sanitize_string(sample_string)
    print(result)