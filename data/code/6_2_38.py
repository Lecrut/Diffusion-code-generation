def weight_difference_generator(weight_pairs):
    for pair in weight_pairs:
        yield abs(pair[0] - pair[1])

if __name__ == '__main__':
    sample_weights = [(70, 65), (80, 85), (90, 88)]
    differences = list(weight_difference_generator(sample_weights))
    print(differences)