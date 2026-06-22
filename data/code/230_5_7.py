def unique_lengths(string_set):
    lengths = set(len(s) for s in string_set)
    return sorted(lengths)

if __name__ == '__main__':
    sample_set = {"hello", "world", "python", "code"}
    print(unique_lengths(sample_set))