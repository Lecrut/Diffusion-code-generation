def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return [char for char, count in char_count.items() if count > 1]
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)