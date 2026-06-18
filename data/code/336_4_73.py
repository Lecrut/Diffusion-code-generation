def find_duplicates(s):
    char_count = {}
    duplicates = []
    for char in s:
        if char in char_count:
            count = char_count[char] + 1
            if count == 2 and not (char, False) in [(d[0], d[1]) for d in duplicates]:
                duplicates.append((char, True))
        else:
            char_count[char] = 1
    return [c[0].lower() for c in sorted(duplicates)]
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)