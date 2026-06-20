def trim_whitespace(input_str: str) -> str:
    return input_str.strip()

if __name__ == '__main__':
    sample_input = "   hello world   "
    result = trim_whitespace(sample_input)
    print(result)