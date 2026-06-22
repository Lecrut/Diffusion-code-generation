def generate_substrings(s):
    n = len(s)
    for start in range(n):
        for end in range(start + 1, n + 1):
            yield s[start:end]

if __name__ == '__main__':
    sample_string = "hello"
    substrings_gen = generate_substrings(sample_string)
    print("Substrings of 'hello':")
    for sub in substrings_gen:
        print(sub)

    long_sample_string = "abcdefghij"
    long_substrings_gen = generate_substrings(long_sample_string)
    print("\nSubstrings of 'abcdefghij':")
    for sub in long_substrings_gen:
        print(sub)