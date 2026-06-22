def sanitize_to_float(text: str) -> float:
    digits = "".join(c for c in text if c.isdigit())
    if not digits:
        return 0.0
    return float(digits)

if __name__ == '__main__':
    sample_inputs = ["abc123def", "no digits here", "42", "99.88", "a1b2c3", ""]
    for s in sample_inputs:
        result = sanitize_to_float(s)
        print(f"Input: {s!r} -> Output: {result}")