def generate_substrings(s):
    n = len(s)
    for start_index in range(n):
        for end_index in range(start_index, n):
            yield s[start_index:end_index + 1]

if __name__ == '__main__':
    sample_input = "hello"
    substrings = list(generate_substrings(sample_input))
    print(substrings)