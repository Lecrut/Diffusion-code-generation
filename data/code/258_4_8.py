def average_pairs(pair_dict):
    return {pair: (values[0] + values[1]) / 2 for pair, values in pair_dict.items()}

if __name__ == '__main__':
    sample_dict = {
        ('a', 'b'): [3, 5],
        ('c', 'd'): [4, 8],
        ('e', 'f'): [6, 10]
    }
    print(average_pairs(sample_dict))