def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for char in s:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return [char for char, count in char_count.items() if count > 1]
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)