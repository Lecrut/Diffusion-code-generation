def find_duplicate_chars(s: str) -> list[str]:
    char_count = {}
    for char in s:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    duplicates = []
    seen_duplicates = set()
    for char in sorted(set(s)):
        count = char_count.get(char, 0)
        if count > 1 and char not in seen_duplicates:
            duplicates.append(char.lower())
            seen_duplicates.add(char.lower())
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_chars(sample_string)
    print(result)