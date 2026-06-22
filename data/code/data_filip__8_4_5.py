def split_and_strip_tokens(input_string: str) -> list:
    return [token.strip() for token in input_string.split(',')]

if __name__ == '__main__':
    sample_text = "  apple , banana , cherry , date  "
    result = split_and_strip_tokens(sample_text)
    print(result)