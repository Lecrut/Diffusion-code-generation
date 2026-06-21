if __name__ == '__main__':
    strings = ["apple", "bee", "cat", "dog", "elephant"]
    grouped_by_length = {len(s): [s for s in strings if len(s) == k] for k in set(len(s) for s in strings)}
    print(grouped_by_length)