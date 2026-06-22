def extract_numeric_string(s: str) -> str:
    return ''.join([c for c in s if c.isdigit()])

if __name__ == '__main__':
    text = "abc123xyz456"
    result = extract_numeric_string(text)
    print(result)