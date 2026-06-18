def find_duplicate_chars(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if ch.lower() not in char_count:
            char_count[ch.lower()] = 0
        char_count[ch.lower()] += 1
    duplicates = []
    seen_duplicates = set()
    for ch, count in sorted(char_count.items()):
        if count > 1 and ch not in seen_duplicates:
            duplicates.append(ch)
            seen_duplicates.add(ch)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_chars(sample_string)
    print(result)