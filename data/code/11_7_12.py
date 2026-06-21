def find_repeated_chars(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return ''.join(sorted(repeated))

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "programming"
    sample3 = "abcdef"
    sample4 = "aabbcc"
    print(find_repeated_chars(sample1))
    print(find_repeated_chars(sample2))
    print(find_repeated_chars(sample3))
    print(find_repeated_chars(sample4))