def strip_whitespace(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample_text = '   hello world   '
    result = strip_whitespace(sample_text)
    print(repr(result))