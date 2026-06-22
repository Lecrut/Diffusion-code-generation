def find_repeated_characters(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return ''.join(sorted(repeated))

if __name__ == '__main__':
    print(find_repeated_characters("hello"))
    print(find_repeated_characters("programming"))
    print(find_repeated_characters("abcdef"))
    print(find_repeated_characters("aabbcc"))