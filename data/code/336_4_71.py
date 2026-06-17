def find_duplicate_characters(s: str) -> list[str]:
    char_count = {}
    for char in s:
        if not char.isalnum():
            continue
        char_count[char] = char_count.get(char, 0) + 1
    duplicates = [char for char, count in char_count.items() if count > 1]
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_characters(sample_string)
    print(result)