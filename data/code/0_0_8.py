def extract_digits(s: str) -> int:
    digits = ''.join(c for c in s if c.isdigit())
    if not digits:
        return 0
    return int(digits)

if __name__ == '__main__':
    test_cases = [
        "abc123def45",
        "no_digits_here",
        "9999",
        "",
        "a0b0c0",
        "mixed123text456end789"
    ]
    for case in test_cases:
        result = extract_digits(case)
        print(f"Input: '{case}' -> Output: {result}")