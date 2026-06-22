def find_repeated_characters(s: str) -> list:
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    return [char for char, cnt in count.items() if cnt > 1]

if __name__ == '__main__':
    print(find_repeated_characters("hello"))
    print(find_repeated_characters("abcabc"))
    print(find_repeated_characters("unique"))
    print(find_repeated_characters("aabbcc"))