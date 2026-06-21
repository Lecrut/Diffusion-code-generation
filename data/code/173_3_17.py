def group_by_length(strings):
    return {len(s): [s for s in strings if len(s) == l] for l in set(len(s) for s in strings)}

if __name__ == '__main__':
    sample_strings = ["apple", "bee", "cat", "dog", "elephant"]
    print(group_by_length(sample_strings))