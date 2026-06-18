def find_duplicate_chars(s: str) -> list[str]:
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    duplicates = [char for char, count in char_count.items() if count > 1]
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_chars(sample_string)
    print(result)