def generate_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield s[i:j]

if __name__ == '__main__':
    sample_string = "xyz"
    all_substrings = list(generate_substrings(sample_string))
    print(all_substrings)

    another_sample_string = "hello"
    more_substrings = list(generate_substrings(another_sample_string))
    print(more_substrings)