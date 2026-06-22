def unique_lengths(string_set):
    if not isinstance(string_set, set):
        raise ValueError("Input must be a set of strings")
    lengths = {len(s) for s in string_set}
    return sorted(lengths)

if __name__ == '__main__':
    sample_set = {"apple", "banana", "cherry", "date"}
    print(unique_lengths(sample_set))