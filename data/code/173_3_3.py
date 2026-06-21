if __name__ == '__main__':
    strings = ["apple", "bee", "cat", "dog", "elephant"]
    grouped_by_length = {len(s): [s for s in strings if len(s) == len_] for len_ in set(len(s) for s in strings)}
    print(grouped_by_length)