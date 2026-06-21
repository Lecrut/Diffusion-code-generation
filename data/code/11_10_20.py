def find_repeated_characters(s: str) -> list:
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    repeated = []
    seen = set()
    for char in s:
        if char_count[char] > 1 and char not in seen:
            repeated.append(char)
            seen.add(char)
    return repeated

if __name__ == '__main__':
    print(find_repeated_characters("programming"))
    print(find_repeated_characters("hello"))
    print(find_repeated_characters("abcdef"))
    print(find_repeated_characters("aabbccdd"))