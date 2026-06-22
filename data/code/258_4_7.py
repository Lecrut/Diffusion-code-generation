def average_pairs(pair_dict):
    return {pair: (pair_dict[pair][0] + pair_dict[pair][1]) / 2 for pair in pair_dict}

if __name__ == '__main__':
    sample_data = {
        ('a', 'b'): [3, 5],
        ('c', 'd'): [7, 9]
    }
    print(average_pairs(sample_data))