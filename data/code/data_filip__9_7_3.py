def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        return str(text).strip()
    return text.strip()

if __name__ == '__main__':
    sample_text = "   Hello, World!   "
    result = normalize_text(sample_text)
    print(result)