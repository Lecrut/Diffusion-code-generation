def find_duplicate_characters(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if ch.isalpha():
            char_count[ch] = char_count.get(ch, 0) + 1
    duplicates = []
    seen_in_result = set()
    for ch, count in char_count.items():
        if count > 1 and ch not in seen_in_result:
            duplicates.append(ch)
            seen_in_result.add(ch)
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_characters(sample_string)
    print(result)