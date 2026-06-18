def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for char in s.lower():
        if not char.isalpha() and char != ' ':
            continue
        char_count[char] = char_count.get(char, 0) + 1
    duplicates = [char for char, count in char_count.items() if count > 1]
    return sorted(list(set(duplicates)))
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)