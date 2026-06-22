def unique_lengths(string_set):
    return sorted({len(s) for s in string_set})

if __name__ == '__main__':
    sample_set = {"apple", "banana", "cherry", "date"}
    print(unique_lengths(sample_set))