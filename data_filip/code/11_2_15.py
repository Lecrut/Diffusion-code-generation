def extract_repeated_characters(text):
    if not text:
        return []
    seen = set()
    duplicates = set()
    for char in text:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return sorted(duplicates)

if __name__ == '__main__':
    sample_text = "programming"
    result = extract_repeated_characters(sample_text)
    print(result)