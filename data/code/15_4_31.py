def pair_match_generator(pairs, value1, value2):
    for pair in pairs:
        if pair == (value1, value2) or pair == (value2, value1):
            yield True

if __name__ == '__main__':
    sample_pairs = [(1, 2), (3, 4), (5, 6), (2, 1)]
    value1 = 1
    value2 = 2
    
    for match in pair_match_generator(sample_pairs, value1, value2):
        print(match)