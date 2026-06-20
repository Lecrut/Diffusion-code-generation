def extract_repeated_characters(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return sorted(list(repeated))

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "programming",
        "abcdef",
        "aabbccddeeff",
        "mississippi"
    ]
    for sample in sample_strings:
        print(extract_repeated_characters(sample))