def generate_substrings(s):
    n = len(s)
    for start_index in range(n):
        for end_index in range(start_index + 1, n + 1):
            yield s[start_index:end_index]

if __name__ == '__main__':
    sample_input = "hello"
    substrings = list(generate_substrings(sample_input))
    print(substrings)