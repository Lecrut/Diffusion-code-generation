def average_pairs(pair_list):
    return [sum(pair) / 2 for pair in pair_list]

if __name__ == '__main__':
    sample_values = [(4, 6), (8, 10), (12, 14)]
    print(average_pairs(sample_values))