def extract_digits(s: str) -> str:
    return ''.join(c for c in s if c.isdigit())

if __name__ == '__main__':
    sample_strings = [
        "abc123def456",
        "hello world! @# 789",
        "no digits here",
        "0.123-456+789",
        "  ",
        "a1b2c3d4e5",
    ]
    for s in sample_strings:
        print(extract_digits(s))