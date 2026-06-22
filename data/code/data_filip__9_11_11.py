def trim_string(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample_text = "  hello world  "
    result = trim_string(sample_text)
    print(result)