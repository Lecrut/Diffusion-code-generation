def find_repeated_characters(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return list(repeated)

if __name__ == '__main__':
    sample_strings = ["hello", "programming", "abcde", "aabbcc", ""]
    for s in sample_strings:
        print(find_repeated_characters(s))