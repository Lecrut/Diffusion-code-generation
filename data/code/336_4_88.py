def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for c in s:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    duplicates = []
    seen_chars = set()
    for c, count in char_count.items():
        if count > 1 and c not in seen_chars:
            duplicates.append(c)
            seen_chars.add(c)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)