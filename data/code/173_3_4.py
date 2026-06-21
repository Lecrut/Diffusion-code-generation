if __name__ == '__main__':
    sample_strings = ["apple", "bee", "cat", "dog", "elephant"]
    grouped_by_length = {len(s): [s for s in sample_strings if len(s) == len_] for len_ in set(len(s) for s in sample_strings)}
    print(grouped_by_length)