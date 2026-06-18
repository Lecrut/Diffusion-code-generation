def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for char in s:
        if char.isalpha():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    duplicates = []
    seen = set()
    for char, count in char_count.items():
        if count > 1 and char not in seen:
            duplicates.append(char)
            seen.add(char)
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)