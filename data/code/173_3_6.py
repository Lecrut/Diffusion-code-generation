if __name__ == '__main__':
    STRINGS = ["apple", "bee", "cat", "dog", "elephant"]
    GROUPED_BY_LENGTH = {len(s): [s for s in STRINGS if len(s) == l] for l in set(len(s) for s in STRINGS)}
    print(GROUPED_BY_LENGTH)