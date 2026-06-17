def find_duplicates(s: str) -> list[str]:
    char_count = {}
    duplicates = []
    for char in s.lower():
        if not char.isalpha() and len(char) > 1:
            continue
        count = char_count.get(char, 0) + 1
        char_count[char] = count
        if count == 2 and char not in duplicates:
            duplicates.append(char)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world this is a test"
    result = find_duplicates(sample_string)
    print(result)