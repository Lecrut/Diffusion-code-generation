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
    sample1 = "hello world"
    print(find_repeated_characters(sample1))
    sample2 = "programming"
    print(find_repeated_characters(sample2))
    sample3 = "abcdef"
    print(find_repeated_characters(sample3))