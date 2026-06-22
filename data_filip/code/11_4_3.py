def find_duplicate_chars(text: str) -> list:
    if not text:
        return []
    lower_text = text.lower()
    char_counts = {}
    for char in lower_text:
        char_counts[char] = char_counts.get(char, 0) + 1
    duplicates = sorted([char for char, count in char_counts.items() if count > 1])
    return duplicates

if __name__ == '__main__':
    sample_text = "Hello World"
    result = find_duplicate_chars(sample_text)
    print(result)