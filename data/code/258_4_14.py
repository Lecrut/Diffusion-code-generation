def average_pairs(pair_dict):
    return {pair: (a + b) / 2 for pair, (a, b) in pair_dict.items()}

if __name__ == '__main__':
    sample_dict = {
        ('x', 'y'): (10, 20),
        ('a', 'b'): (30, 40),
        ('c', 'd'): (50, 60)
    }
    print(average_pairs(sample_dict))