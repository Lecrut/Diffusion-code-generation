def find_repeated_chars(s):
    seen = set()
    repeated = []
    for char in s:
        if char in seen and char not in repeated:
            repeated.append(char)
        else:
            seen.add(char)
    return repeated

if __name__ == '__main__':
    print(find_repeated_chars("programming"))
    print(find_repeated_chars("hello"))
    print(find_repeated_chars("abcabc"))
    print(find_repeated_chars("abcdef"))
    print(find_repeated_chars("aabbcc"))