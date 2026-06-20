def trim_whitespace(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample_data = "   Hello World   "
    result = trim_whitespace(sample_data)
    print(result)