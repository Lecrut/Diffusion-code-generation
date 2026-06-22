def unique_lengths(strings):
    lengths = {len(s) for s in strings}
    return sorted(lengths)

if __name__ == '__main__':
    sample_strings = {"hello", "world", "a", "Python", "code"}
    print(unique_lengths(sample_strings))