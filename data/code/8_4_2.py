def split_and_strip_tokens(s: str) -> list:
    return [token.strip() for token in s.split(',')]

if __name__ == '__main__':
    sample_string = "  apple , banana , orange  , grape "
    result = split_and_strip_tokens(sample_string)
    print(result)