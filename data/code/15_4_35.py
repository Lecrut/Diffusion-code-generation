def pair_match_generator(value1, value2, pairs):
    for pair in pairs:
        if pair[0] == value1 and pair[1] == value2:
            yield True

if __name__ == '__main__':
    sample_value1 = 'apple'
    sample_value2 = 'banana'
    sample_pairs = [('apple', 'banana'), ('orange', 'grape'), ('apple', 'orange')]

    for match in pair_match_generator(sample_value1, sample_value2, sample_pairs):
        print(match)