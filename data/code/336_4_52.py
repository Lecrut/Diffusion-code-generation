def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for char in s:
        if not char.isalnum():
            continue
        count = char_count.get(char, 0) + 1
        if count == 2:
            return [char]
        elif count > 2 and len([c for c in char_count.values() if c >= 2]) < 3:
            pass
    duplicates = []
    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)