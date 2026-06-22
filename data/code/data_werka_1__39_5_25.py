def generate_substrings(s):
    n = len(s)
    for start in range(n):
        for end in range(start + 1, n + 1):
            yield s[start:end]

if __name__ == '__main__':
    SAMPLE_STRING_SHORT = "abc"
    SAMPLE_STRING_LONG = "abcdefg"

    print("Substrings of '{}':".format(SAMPLE_STRING_SHORT))
    for sub in generate_substrings(SAMPLE_STRING_SHORT):
        print(sub)

    print("\nSubstrings of '{}':".format(SAMPLE_STRING_LONG))
    for sub in generate_substrings(SAMPLE_STRING_LONG):
        print(sub)