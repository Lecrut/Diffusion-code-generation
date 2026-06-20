def trim_whitespace(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    result = trim_whitespace("   Hello, World!   ")
    print(result)