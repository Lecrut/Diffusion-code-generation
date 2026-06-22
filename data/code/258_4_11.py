def average_pairs(pair_dict):
    return {pair: (pair[0] + pair[1]) / 2 for pair in pair_dict}

if __name__ == '__main__':
    sample_dict = {(1, 2): 3, (4, 5): 9, (6, 7): 13}
    print(average_pairs(sample_dict))