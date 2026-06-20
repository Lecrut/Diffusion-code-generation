def weight_diff_generator(weight_pairs):
    for pair in weight_pairs:
        yield pair[0] - pair[1]

if __name__ == '__main__':
    sample_pairs = [(100, 95), (80, 85), (120, 115), (90, 90)]
    diffs = list(weight_diff_generator(sample_pairs))
    print(diffs)