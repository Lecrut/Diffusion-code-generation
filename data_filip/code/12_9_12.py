def validate_international_dialing_code(code: str) -> bool:
    if not isinstance(code, str):
        raise TypeError("Input must be a string")
    stripped = code.strip()
    if not stripped:
        return False
    if stripped.startswith('+'):
        digits_part = stripped[1:]
    else:
        digits_part = stripped
    if not digits_part.isdigit():
        return False
    if len(digits_part) < 1 or len(digits_part) > 4:
        return False
    return True

if __name__ == '__main__':
    samples = ["+1", "+44", "+86", "+91", "+7", "+39", "1", "44", "+", "+abc", "+12345", "", " ", "+ 1", "+1a"]
    results = [validate_international_dialing_code(s) for s in samples]
    print(list(zip(samples, results)))