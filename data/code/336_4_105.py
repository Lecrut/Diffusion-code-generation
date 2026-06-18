def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if not (ch.isalpha()):
            continue
        char_count[ch] = char_count.get(ch, 0) + 1
    duplicates = []
    seen_chars = set()
    for ch in sorted(char_count.keys()):
        count = char_count[ch]
        if count > 1 and ch not in seen_chars:
            duplicates.append(ch)
            seen_chars.add(ch)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)