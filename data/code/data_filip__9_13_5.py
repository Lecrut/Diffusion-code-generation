def trim_whitespace(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    sample_text = "  hello world  "
    result = trim_whitespace(sample_text)
    print(result)