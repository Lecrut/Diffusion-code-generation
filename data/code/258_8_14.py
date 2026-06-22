def average_pairs(pair_generator):
    return tuple((a + b) / 2 for a, b in pair_generator)

if __name__ == '__main__':
    sample_gen = ((1, 2), (3, 4), (5, 6))
    print(average_pairs(sample_gen))