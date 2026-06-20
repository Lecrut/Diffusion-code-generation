def split_and_strip_tokens(text: str) -> list:
    return [token.strip() for token in text.split(',')]

if __name__ == '__main__':
    sample_input = "  apple , banana  , cherry  , date "
    result = split_and_strip_tokens(sample_input)
    print(result)