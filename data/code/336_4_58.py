def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if not (ch.isalpha() or ch.isdigit()):
            continue
        char_count[ch] = char_count.get(ch, 0) + 1
    duplicates = []
    for ch, count in char_count.items():
        if count > 1 and ch not in duplicates:
            duplicates.append(ch)
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)