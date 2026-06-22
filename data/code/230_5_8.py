def unique_lengths(string_set):
    if not isinstance(string_set, set) or not all(isinstance(s, str) for s in string_set):
        raise ValueError("Input must be a set of strings")
    
    lengths = set(len(s) for s in string_set)
    return sorted(lengths)

if __name__ == '__main__':
    sample_set = {"apple", "banana", "cherry", "date"}
    print(unique_lengths(sample_set))