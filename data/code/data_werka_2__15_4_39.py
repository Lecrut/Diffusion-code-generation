def match_generator(value1, value2, pairs):
    for pair in pairs:
        if (pair[0] == value1 and pair[1] == value2) or (pair[0] == value2 and pair[1] == value1):
            yield True

if __name__ == '__main__':
    sample_pairs = [('x', 'y'), ('z', 'w'), ('v', 'u'), ('y', 'x')]
    for match in match_generator('x', 'y', sample_pairs):
        print(match)