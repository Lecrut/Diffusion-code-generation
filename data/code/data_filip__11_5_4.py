def detect_repeated_characters(s):
    seen = set()
    repeated = []
    for char in s:
        if char in seen and char not in repeated:
            repeated.append(char)
        else:
            seen.add(char)
    return repeated

if __name__ == '__main__':
    print(detect_repeated_characters("programming"))
    print(detect_repeated_characters("hello"))
    print(detect_repeated_characters("abcdefg"))
    print(detect_repeated_characters("aabbbccc"))
    print(detect_repeated_characters(""))
    print(detect_repeated_characters("a"))