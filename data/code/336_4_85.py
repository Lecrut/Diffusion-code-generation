def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if ch.isalpha():
            char_count[ch] = char_count.get(ch, 0) + 1
    duplicates = [ch for ch, count in char_count.items() if count > 1]
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)