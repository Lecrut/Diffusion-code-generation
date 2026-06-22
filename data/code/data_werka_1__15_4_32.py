def match_generator(value1, value2, pairs_list):
    for pair in pairs_list:
        if pair == (value1, value2) or pair == (value2, value1):
            yield True

if __name__ == '__main__':
    sample_pairs = [('a', 'b'), ('c', 'd'), ('e', 'f'), ('b', 'a')]
    value1 = 'a'
    value2 = 'b'
    
    for match in match_generator(value1, value2, sample_pairs):
        print(match)