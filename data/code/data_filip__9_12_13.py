def trim_spaces(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample_text = "  hello world  "
    result = trim_spaces(sample_text)
    print(result)