def group_by_length(strings):
    lengths = {len(s) for s in strings}
    return {length: [s for s in strings if len(s) == length] for length in lengths}

if __name__ == '__main__':
    sample_strings = ["apple", "bee", "cat", "dog", "elephant"]
    grouped_by_length = group_by_length(sample_strings)
    print(grouped_by_length)