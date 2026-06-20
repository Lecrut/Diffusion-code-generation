def split_and_trim(text: str) -> list:
    if not text:
        return []
    parts = text.split(',')
    trimmed = [part.strip() for part in parts]
    return trimmed

if __name__ == '__main__':
    sample_text = "  hello , world ,  python "
    result = split_and_trim(sample_text)
    print(result)