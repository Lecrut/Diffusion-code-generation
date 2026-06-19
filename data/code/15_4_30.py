def match_generator(value1, value2, pairs):
    for pair in pairs:
        if pair == (value1, value2) or pair == (value2, value1):
            yield True

if __name__ == '__main__':
    sample_pairs = [(1, 2), (3, 4), (5, 6), (2, 1)]
    generator = match_generator(1, 2, sample_pairs)
    for result in generator:
        print(result)