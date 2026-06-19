def match_generator(value1, value2, pairs):
    for pair in pairs:
        if pair == (value1, value2):
            yield True

if __name__ == '__main__':
    sample_pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
    gen = match_generator(3, 4, sample_pairs)
    for result in gen:
        print(result)