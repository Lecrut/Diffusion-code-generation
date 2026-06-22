def split_and_strip(text: str) -> list[str]:
    return [token.strip() for token in text.split(",") if token.strip()]

if __name__ == '__main__':
    sample_input = "  hello , world , python ,  "
    result = split_and_strip(sample_input)
    print(result)