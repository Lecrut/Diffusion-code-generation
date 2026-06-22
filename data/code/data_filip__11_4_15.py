def find_duplicate_chars(text):
    if not isinstance(text, str):
        return []
    text_lower = text.lower()
    counts = {}
    for char in text_lower:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    duplicates = [char for char, count in counts.items() if count > 1]
    duplicates.sort()
    return duplicates

if __name__ == '__main__':
    sample_text = "Hello World"
    result = find_duplicate_chars(sample_text)
    print(result)