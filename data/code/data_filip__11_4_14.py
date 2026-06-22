def find_duplicate_characters(text):
    if not text:
        return set()
    seen = set()
    duplicates = set()
    normalized_text = text.lower()
    for char in normalized_text:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return duplicates

if __name__ == '__main__':
    sample_string = "Programming"
    result = find_duplicate_characters(sample_string)
    print(result)