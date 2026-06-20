def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    stripped = text.strip()
    return stripped

if __name__ == '__main__':
    sample_text = "  Hello, World!  "
    result = normalize_text(sample_text)
    print(result)