def find_repeated_characters(s):
    seen = set()
    duplicates = set()
    for char in s:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return "".join(sorted(duplicates))

if __name__ == '__main__':
    print(find_repeated_characters("programming"))
    print(find_repeated_characters("hello"))
    print(find_repeated_characters("abcdef"))