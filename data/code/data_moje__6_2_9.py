def weight_difference_generator(pairs):
    for w1, w2 in pairs:
        yield w1 - w2

if __name__ == '__main__':
    sample_pairs = [(100, 50), (200, 150), (50, 100)]
    generator = weight_difference_generator(sample_pairs)
    print(list(generator))