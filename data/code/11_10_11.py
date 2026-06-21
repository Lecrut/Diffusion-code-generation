def find_repeated_characters(s: str) -> list:
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return [char for char, count in char_count.items() if count > 1]

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "programming",
        "abcdefg",
        "aabbccdd",
        "hello world"
    ]
    for sample in sample_strings:
        print(find_repeated_characters(sample))