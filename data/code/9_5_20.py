def normalize_whitespace(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.strip()

if __name__ == '__main__':
    sample_text = "\t  \n  Excessive    Whitespace  Here  \n\t  "
    cleaned = normalize_whitespace(sample_text)
    print(cleaned)