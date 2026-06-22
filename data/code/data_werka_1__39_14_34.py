def generate_substrings(s):
    n = len(s)
    for start in range(n):
        for end in range(start + 1, n + 1):
            yield s[start:end]

if __name__ == '__main__':
    SAMPLE_STRING_1 = "abc"
    SAMPLE_STRING_2 = "a"
    SAMPLE_STRING_3 = "ab"

    print(list(generate_substrings(SAMPLE_STRING_1)))
    print(list(generate_substrings(SAMPLE_STRING_2)))
    print(list(generate_substrings(SAMPLE_STRING_3)))