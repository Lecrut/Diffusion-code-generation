def generate_substrings(s):
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield s[start:end]
if __name__ == '__main__':
    sample_string = 'hello'
    substrings_generator = generate_substrings(sample_string)
    all_substrings = list(substrings_generator)
    print(all_substrings)
    long_sample_string = 'abcdefghijklmnopqrstuvwxyz'
    long_substrings_generator = generate_substrings(long_sample_string)
    long_all_substrings = list(long_substrings_generator)
    for substring in long_all_substrings[:10]:
        print(substring)