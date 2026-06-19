def generate_substrings(s):
    n = len(s)
    for start in range(n):
        for end in range(start + 1, n + 1):
            yield s[start:end]

if __name__ == '__main__':
    SAMPLE_STRING = "abc"
    SUBSTRING_GENERATOR = generate_substrings(SAMPLE_STRING)
    ALL_SUBSTRINGS = list(SUBSTRING_GENERATOR)
    print(ALL_SUBSTRINGS)

    ANOTHER_SAMPLE_STRING = "xyz"
    ANOTHER_SUBSTRING_GENERATOR = generate_substrings(ANOTHER_SAMPLE_STRING)
    ANOTHER_ALL_SUBSTRINGS = list(ANOTHER_SUBSTRING_GENERATOR)
    print(ANOTHER_ALL_SUBSTRINGS)