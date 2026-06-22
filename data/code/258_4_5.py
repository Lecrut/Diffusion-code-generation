def average_pairs(pair_dict):
    return {pair: (a + b) / 2 for pair, (a, b) in pair_dict.items()}

if __name__ == '__main__':
    sample_dict = {
        ('apple', 'banana'): (1.0, 2.5),
        ('carrot', 'date'): (3.0, 4.0),
        ('eggplant', 'fig'): (5.5, 6.5)
    }
    print(average_pairs(sample_dict))