def weight_difference_generator(weight_pairs):
    for pair in weight_pairs:
        yield abs(pair[0] - pair[1])

if __name__ == '__main__':
    sample_pairs = [(100, 95), (70, 82), (65, 65), (90, 110)]
    differences = list(weight_difference_generator(sample_pairs))
    print(differences)