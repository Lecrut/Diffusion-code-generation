def trim_whitespace(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample_string = "  Hello, World!  "
    result = trim_whitespace(sample_string)
    print(result)