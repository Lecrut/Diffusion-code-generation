def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if ch not in char_count:
            char_count[ch] = 1
        else:
            char_count[ch] += 1
    duplicates = []
    seen = set()
    sorted_chars = sorted(char_count.keys())
    for ch in sorted_chars:
        if char_count[ch] > 1 and ch not in seen:
            duplicates.append(ch)
            seen.add(ch)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)