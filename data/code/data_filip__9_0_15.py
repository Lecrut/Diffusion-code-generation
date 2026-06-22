def strip_whitespace(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample_input = "   Hello World   "
    result = strip_whitespace(sample_input)
    print(result)