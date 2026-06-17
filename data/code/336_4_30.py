def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if ch.lower() not in char_count:
            char_count[ch.lower()] = 0
        char_count[ch.lower()] += 1
    duplicates = []
    seen_chars = set()
    for ch, count in sorted(char_count.items()):
        if count > 1 and ch not in seen_chars:
            duplicates.append(ch)
            seen_chars.add(ch)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)