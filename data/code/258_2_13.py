def average_pairs(pair_list):
    return [sum(pair) / 2 for pair in pair_list]

if __name__ == '__main__':
    sample_values = [(1, 2), (3, 4), (5, 6)]
    print(average_pairs(sample_values))