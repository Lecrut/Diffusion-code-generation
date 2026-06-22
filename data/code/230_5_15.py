def unique_lengths(string_set):
    lengths = set()
    for s in string_set:
        lengths.add(len(s))
    return sorted(lengths)

if __name__ == '__main__':
    sample_set = {"hello", "world", "python", "programming"}
    result = unique_lengths(sample_set)
    print(result)