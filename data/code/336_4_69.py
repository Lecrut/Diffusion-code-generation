def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if ch.isalpha():
            char_count[ch] = char_count.get(ch, 0) + 1
    duplicates = []
    seen = set()
    for ch, count in sorted(char_count.items()):
        if count > 1 and ch not in seen:
            duplicates.append(ch)
            seen.add(ch)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)