def average_pairs(generator):
    return tuple((a + b) / 2 for a, b in generator)

if __name__ == '__main__':
    sample_pairs = ((1, 2), (3, 4), (5, 6))
    print(average_pairs(sample_pairs))