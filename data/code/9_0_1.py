def strip_whitespace(input_string: str) -> str:
    return input_string.strip()

if __name__ == '__main__':
    result = strip_whitespace("  hello world  ")
    print(result)