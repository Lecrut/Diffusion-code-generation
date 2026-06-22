def sanitize_to_float(text: str) -> float:
    digits = ''.join(c for c in text if c.isdigit())
    if not digits:
        return 0.0
    return float(digits)

if __name__ == '__main__':
    sample_input = "abc123.45xyz"
    result = sanitize_to_float(sample_input)
    print(result)