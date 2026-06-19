def match_generator(value1, value2, pairs):
    for pair in pairs:
        if pair[0] == value1 and pair[1] == value2:
            yield True

if __name__ == '__main__':
    sample_pairs = [('a', 'b'), ('c', 'd'), ('e', 'f'), ('a', 'b')]
    result = list(match_generator('a', 'b', sample_pairs))
    print(result)