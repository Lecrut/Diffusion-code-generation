def average_pairs(pair_dict):
    return {pair: (pair[0] + pair[1]) / 2 for pair in pair_dict.keys()}

if __name__ == '__main__':
    sample_dict = {(1, 2): 3, (4, 5): 9}
    print(average_pairs(sample_dict))