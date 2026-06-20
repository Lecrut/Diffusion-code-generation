def weight_difference_generator(weight_pairs):
    for w1, w2 in weight_pairs:
        yield abs(w1 - w2)

if __name__ == '__main__':
    sample_pairs = [(70, 80), (55, 55), (90, 85), (100, 110)]
    differences = list(weight_difference_generator(sample_pairs))
    print(differences)