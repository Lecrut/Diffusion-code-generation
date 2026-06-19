def generate_substrings(s):
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield s[start:end]

if __name__ == '__main__':
    sample_string = "hello"
    substrings_gen = generate_substrings(sample_string)
    result = list(substrings_gen)
    print(result)

    long_sample_string = "abcdefghij"
    long_substrings_gen = generate_substrings(long_sample_string)
    long_result = list(long_substrings_gen)
    print(long_result)