def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for char in s:
        if char.lower() not in char_count:
            char_count[char.lower()] = 0
        char_count[char.lower()] += 1
    duplicates = []
    seen = set()
    for char, count in char_count.items():
        if count > 1 and char not in seen:
            duplicates.append(char)
            seen.add(char)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)