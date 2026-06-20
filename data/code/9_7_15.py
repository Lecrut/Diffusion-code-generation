def normalize_text(text: str) -> str:
    result = text.strip()
    return result

if __name__ == '__main__':
    sample_text = "  Hello World  "
    normalized = normalize_text(sample_text)
    print(normalized)