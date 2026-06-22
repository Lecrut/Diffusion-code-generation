def find_duplicate_characters(text: str) -> list:
    lower_text = text.lower()
    seen = set()
    duplicates = set()
    for char in lower_text:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return sorted(list(duplicates))

if __name__ == '__main__':
    sample_text = "Programming"
    result = find_duplicate_characters(sample_text)
    print(result)