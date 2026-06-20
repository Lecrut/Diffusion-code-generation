def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.strip()

if __name__ == '__main__':
    sample_data = "  Hello World  "
    result = normalize_text(sample_data)
    print(repr(result))