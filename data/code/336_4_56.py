def find_duplicate_characters(s: str) -> list[str]:
    char_count = {}
    for ch in s.lower():
        if not ch.isalnum():
            continue
        char_count[ch] = char_count.get(ch, 0) + 1
    duplicates = []
    seen_duplicates = set()
    for ch, count in sorted(char_count.items()):
        if count > 1 and ch not in seen_duplicates:
            duplicates.append(ch)
            seen_duplicates.add(ch)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_characters(sample_string)
    print(result)