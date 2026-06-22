def extract_digits(s: str) -> list:
    return [c for c in s if c.isdigit()]

if __name__ == '__main__':
    result = extract_digits("abc123!@#456")
    print(result)