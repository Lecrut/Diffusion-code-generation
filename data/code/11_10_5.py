def find_repeated_characters(s: str) -> list:
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return [char for char, count in char_count.items() if count > 1]

if __name__ == '__main__':
    print(find_repeated_characters("hello world"))
    print(find_repeated_characters("abcdef"))
    print(find_repeated_characters("aabbcc"))
    print(find_repeated_characters(""))