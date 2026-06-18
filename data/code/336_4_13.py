def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if ch not in char_count:
            char_count[ch] = 0
        char_count[ch] += 1
    duplicates = []
    seen_dups = set()
    for ch, count in char_count.items():
        if count > 1 and ch not in seen_dups:
            duplicates.append(ch)
            seen_dups.add(ch)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)