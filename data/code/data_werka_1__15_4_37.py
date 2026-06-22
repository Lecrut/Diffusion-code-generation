def match_generator(value1, value2, pairs):
    for pair in pairs:
        if pair[0] == value1 and pair[1] == value2:
            yield True

if __name__ == '__main__':
    sample_pairs = [('apple', 'banana'), ('orange', 'grape'), ('apple', 'orange')]
    value1 = 'apple'
    value2 = 'orange'
    
    for match in match_generator(value1, value2, sample_pairs):
        print(match)