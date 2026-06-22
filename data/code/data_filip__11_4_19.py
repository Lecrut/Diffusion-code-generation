def find_duplicate_chars(text: str) -> list:
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
    sample_text = "Programming is fun, isn't it? Programming is great!"
    result = find_duplicate_chars(sample_text)
    print(result)