def replace_whitespace_with_underscores(text: str) -> str:
    return text.replace(" ", "_")

if __name__ == '__main__':
    sample_text = "hello world  python   code"
    result = replace_whitespace_with_underscores(sample_text)
    print(result)