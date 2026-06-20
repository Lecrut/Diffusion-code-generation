def normalize_text(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample_input = "   Hello World   "
    result = normalize_text(sample_input)
    print(result)