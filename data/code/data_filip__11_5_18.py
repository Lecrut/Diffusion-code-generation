def find_repeated_characters(s):
    seen = set()
    repeated = []
    for char in s:
        if char in seen and char not in repeated:
            repeated.append(char)
        else:
            seen.add(char)
    return repeated

if __name__ == '__main__':
    print(find_repeated_characters("hello"))
    print(find_repeated_characters("programming"))
    print(find_repeated_characters("abc"))
    print(find_repeated_characters("aabbcc"))