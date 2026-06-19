def match_generator(value1, value2, pairs):
    for pair in pairs:
        if pair[0] == value1 and pair[1] == value2:
            yield True
if __name__ == '__main__':
    sample_pairs = [('a', 1), ('b', 2), ('c', 3), ('a', 1)]
    for match in match_generator('a', 1, sample_pairs):
        print(match)