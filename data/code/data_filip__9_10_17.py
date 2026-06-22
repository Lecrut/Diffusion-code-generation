def strip_whitespace(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    result = strip_whitespace("  hello world  ")
    print(result)