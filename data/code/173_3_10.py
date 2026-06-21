sample_strings = ["apple", "bee", "cat", "dog", "elephant"]
grouped_by_length = {len(s): [s for s in sample_strings if len(s) == length] for length in set(len(s) for s in sample_strings)}
if __name__ == '__main__':
    print(grouped_by_length)