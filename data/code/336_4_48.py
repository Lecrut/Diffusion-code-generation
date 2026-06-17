def find_duplicate_chars(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if ch not in char_count:
            char_count[ch] = 0
        char_count[ch] += 1
    duplicates = [ch for ch, count in char_count.items() if count > 1]
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_chars(sample_string)
    print(result)