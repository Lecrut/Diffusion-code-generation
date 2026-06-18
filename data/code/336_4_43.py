def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    duplicates = []
    seen_dups = set()
    for char, count in char_count.items():
        if count > 1 and char not in seen_dups:
            duplicates.append(char)
            seen_dups.add(char)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)