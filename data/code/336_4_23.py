def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for c in s:
        if not c.isalpha():
            continue
        char_count[c] = char_count.get(c, 0) + 1
    return [c for c, count in char_count.items() if count > 1]
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)