def strip_whitespace(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    sample_string = '  Hello, World!  '
    result = strip_whitespace(sample_string)
    print(result)